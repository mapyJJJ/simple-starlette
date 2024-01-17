#### 一个基于asgi协议的api框架，可以快速编写api以及方便使用常见的后端组件，开箱即用

[![License](https://img.shields.io/static/v1?label=asgi&message=starlette&color=red)]()
[![License](https://img.shields.io/static/v1?label=asgi-server&message=uvicorn&color=green)]()
[![License](https://img.shields.io/static/v1?label=imports&message=isort&color=origin)]()
[![License](https://img.shields.io/static/v1?label=format&message=black&color=origin)]()
[![License](https://img.shields.io/static/v1?label=type-hint&message=pyright&color=origin)]()





### 安装使用
---
使用 `pip` 直接安装

```bash
pip install simple-starlette
```

or源码安装
```bash
git clone https://github.com/mapyJJJ/simple-starlette.git
cd simple-starlette
python3 setup.py install
```




### 功能示例
---
这里演示一些常见的场景的使用案例

#### 定义一个api:
```python
from simple_starlette.args import QueryParams
from simple_starlette import SimpleStarlette, Request
from simple_starlette.responses import Response, ResTypeEnum

app = SimpleStarlette(__name__)

@app.route("/ping")
class Ping:
    async def get(self, request: Request):
        return Response("Pong", ResTypeEnum.TEXT)

if __name__ == "__main__":
    app.run()
```

#### api接收query参数或者body参数
> 参数验证基于pydantic，validators等相关用法可查阅文档: https://docs.pydantic.dev/latest/concepts/models/
```python
from typing import List

from simple_starlette.args import QueryParams, BodyParams
from simple_starlette import SimpleStarlette, Request
from simple_starlette.responses import Response, ResTypeEnum

app = SimpleStarlette(__name__)

@register_args
class CommonBody(BodyParams):
    comm_b1: str

@register_args
class CommonQuery(QueryParams):
    comm_q1: str

@app.route("/api")
class Api:
    class Query(QueryParams):
        q1: int
        q2 str

    class Body(BodyParams):
        b1: bool
        b2: List[str]

    async def post(self, request: Request, query_params: Query, body_data: Body, 
                comm_body: CommonBody, comm_query: CommonQuery):
        print(
            query_params.q1, 
            query_params.q2, 
            body_data.b1, 
            body_data.b2, 
            comm_body.comm_b1, 
            comm_query.comm_q1
        )
        return Response("Success", ResTypeEnum.TEXT)
    
if __name__ == "__main__":
    app.run()
```

#### 定义ws接口
```python
from starlette.websockets import WebSocket
from simple_starlette import SimpleStarlette

app = SimpleStarlette(__name__)

@app.route("/ws1", websocket_route=True)
async def test(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data == "close_conn":
            break
        await websocket.send_text(f"receive_text: {data}")

if __name__ == "__main__":
    app.run()
```

#### 使用上下文变量避免参数长传
```python
import json
import typing
from simple_starlette import (g, request, current_app, SimpleStarlette, Request)
from simple_starlette.responses import ResTypeEnum, Response

app = SimpleStarlette(__name__)

@app.route("/")
class Index:
    async def get(self, _: Request):
        g.some_config = {"k": "v"}
        return Response("Success", ResTypeEnum.TEXT)

if __name__ == "__main__":
    app.run()
```

#### 启用在线api文档 
```python
app = SimpleStarlette(
    __name__,
    run_env="dev",  # dev模式开启在线文档
)
```

#### 使用中间件
```python
app = SimpleStarlette(
    __name__,
    middleware=[
        TokenAuthMiddleWareGenFunc( # 鉴权中间件
            validate_process=check_is_login_process,
            on_error=custom_on_error,
            expires=60 * 60,
            httponly=True
        ),
        CorsMiddlewareGenFunc(  # cors
            allow_origins=["http://127.0.0.1:5500"],
            allow_credentials=True,
            allow_methods=("GET","POST",)
        )
    ],
)
```

#### api访问限频
```python
from simple_starlette.middleware.rate_limiter import rate_limit

def user_info_rate_limit_gen(_request: Request):
    if _request.query_params.get("user_id"):
        rate_key = "user_info_%s" % _request.query_params["user_id"]
        return rate_key
    return None

@rate_limit(app, rate_key_factory=user_info_rate_limit_gen,limit_count=5)
@app.route("/user/info")
class UserInfo:
    class Query(QueryParams):
        user_id: int

    async def get(self, request: Request, q: Query):
        return Response({"user_id": q.user_id}, ResTypeEnum.JSON)
```

#### 使用sqlalchemny asyncio
```python
import asyncio
from typing import NamedTuple, cast, List

from sqlalchemy import func


from simple_starlette import (
    Response,
    ResTypeEnum,
    SimpleStarlette,
    Request,
    QueryParams,
    logger,
)
from simple_starlette.db.db_sqlalchemy import (
    BaseModelDict,
    Sqlalchemy,
    column_field,
    register_db_model,
    String,
    Integer,
    row_obj_to_dict,
    select,
    Index,
)

app = SimpleStarlette(__name__)

app.config["DB_URIS"] = {
    "master": "mysql+asyncmy://root:@127.0.0.1:3306/test"
}
logger = logger.getLogger(__name__)

db = Sqlalchemy(app)

@register_db_model
class Person(BaseModelDict):
    id = column_field(Integer, primary_key=True)
    email = column_field(String(64))
    __table_args__ = (Index("idx_email", "email"),)

@app.route("/test_db/add", ["GET"])
class TestDbAdd:
    class PersonParams(QueryParams):
        email: str

    async def get(self, _: Request, person_args: PersonParams):
        async with db.session as session:
            new_person = Person.create_row(email=person_args.email)
            session.add(new_person)
            await session.commit()
            
        return Response(
            {"id": new_person.id, "email": new_person.email},
            ResTypeEnum.JSON,
        )

@app.route("/test_db/list", ["GET"])
async def test_db(request: Request):
    async def query_list():
        async with db.session as session:
            result = await session.execute(select(Person).order_by(Person.id.desc()))
            ps = result.scalars()
        logger.info(ps)
        return ps

    async def query_count():
        async with db.session as session:
            result = await session.execute(select(func.count(Person.id)))
            count = result.scalar()
        return count

    async def query():
        L = await asyncio.gather(
            query_list(), query_count()
        )
        return L

    ps, total_count = await query()
    return Response(
        {"person_list": [row_obj_to_dict(p) for p in ps], "total_count": total_count},
        ResTypeEnum.JSON,
    )

@app.route("/test_db/create_all", allow_methods=["get"])
async def test_db_create_all(request: Request):
    await db.create_all()
    return Response("ok", ResTypeEnum.TEXT)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

#### 使用 lru + TTL 本地缓存
```python
from simple_starlette.cache.memory_cache import (
    LruCache,
    lru_cache_decorator,
    lru_cache_decorator_async,
)

@lru_cache_decorator(maxsize=100, cache_ttl=10 * 60)
def gen_resp(user_id: int):
    ...

@lru_cache_decorator_async(maxsize=100, cache_ttl=10 * 60)
async def gen_resp_async(user_id: int):
    ...
```

#### 使用GuavaCache
```python
from simple_starlette.cache.memory_cache import local_g
from simple_starlette.cache.guava_cache import GuavaCache

def refresh_hot_user_info():
    _d = {}
    # ...
    local_g["user_info"] = _d

gc = GuavaCache(interval=5, refresh_callable=refresh_hot_user_info)
gc.start()
```


#### 
查看更多开发使用实例：[example usage](https://github.com/mapyJJJ/simple-starlette/tree/master/example)

---
#### LICENSE

[GPL-3.0 License](https://github.com/mapyJJJ/simple-starlette/blob/master/LICENSE)

---
