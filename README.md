# Simple-Starlette

### install

`pip install simple-starlette`

### simple example
```python
from starlette.requests import Request
from simple_starlette import SimpleStarlette, Response, ResTypeEnum

app = SimpleStarlette(__name__)


@app.route("/test", allow_methods=["get"])
async def test(request: Request):
    return Response(request.url, ResTypeEnum.TEXT)

app.run()
```

---

### cbv
```python
@app.route("/test")
class Test:
    async def get(self, request: Request):
        return Response(request.url, ResTypeEnum.TEXT)

    async def post(self, request: Request):
        return Response(request.url, ResTypeEnum.TEXT)
```

---

### params
```python
from simple_starlette import BaseModel
@app.route("/test")
class Test:
    class GetArgs(BaseModel):
        name: str
    
    async def get(self, request: Request, params1: GetArgs):
        return Response(params1.name, ResTypeEnum.TEXT)
```

or

```python
from simple_starlette import BaseModel, register_args

@register_args
class GetArgs(BaseModel):
    name: str

@app.route("/test")
async def test(self, request: Request, params1: GetArgs):
    return Response(params1.name, ResTypeEnum.TEXT)
```

---

### include

```python
from starlette.requests import Request
from simple_starlette import (
    SimpleStarlette,
    Response,
    ResTypeEnum,
    BaseModel,
    register_args,
    Include,
)

app = SimpleStarlette(__name__)
api = Include(app, "/api")

@register_args
class GetArgs(BaseModel):
    name: str

@api.route("/test") # /api/test
async def test(self, request: Request, params1: GetArgs):
    return Response(params1.name, ResTypeEnum.TEXT)

app.run()
```

---

### request hook and global var `g`
```python
import time
from starlette.requests import Request
from simple_starlette import SimpleStarlette, Response, ResTypeEnum, g

app = SimpleStarlette(__name__)


@app.before_request
async def _do_before_request(request):
    g.start_time = time.time()


@app.after_request
async def _do_after_request(request, response):
    process_time = time.time() - g.start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.route("/test")
async def test(request: Request):
    print(request.url)
    return Response("test", ResTypeEnum.TEXT)


app.run()
```

---

### exception handle
```python
from simple_starlette.exceptions import SimpleException
from starlette.requests import Request
from simple_starlette import (
    SimpleStarlette,
    register_exception,
    common_exception_handle,
)

app = SimpleStarlette(__name__)


@register_exception
class TestError(SimpleException):
    @staticmethod
    async def exception_handle(request: Request, err: "SimpleException"):
        return await common_exception_handle(request, err)


@app.route("/test")
async def test(request: Request):
    raise TestError(err_msg="test error", status_code=4000)


app.run()
```

---


### websocket
```python
from starlette.websockets import WebSocket
from simple_starlette import SimpleStarlette

app = SimpleStarlette(__name__)


@app.route("/ws", websocket_route=True)
async def test(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"xxx: {data}")

app.run()
```

---

### db(orm:sqlalchemy)
```python
import asyncio

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.sql.elements import Label
from sqlalchemy.sql.functions import count
from starlette.requests import Request


from simple_starlette.db.db_sqlalchemy import DbBaseModel, Sqlalchemy
from simple_starlette import (
    Response,
    ResTypeEnum,
    SimpleStarlette,
    register_args,
    BaseModel,
)

app = SimpleStarlette(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+aiomysql://root:password@localhost/database_name?charset=utf8mb4"

db = Sqlalchemy(app)


class Person(DbBaseModel["Person"]):
    id = Column(Integer, primary_key=True)
    email = Column(String(64))


@register_args
class P(BaseModel):
    email: str


# test query table
@app.route("/test_db", allow_methods=["get"])
async def test_db(request: Request):
    async def query_one_person():
        r = await db.Session.execute(select(Person).order_by(Person.id.desc()))
        fisrt_p = r.scalars().first()
        return fisrt_p

    async def query_person_count():
        r = await db.Session.execute(select(Label("count", count(Person.id))))
        return r.one()

    async def query():
        L = await asyncio.gather(query_one_person(), query_person_count())
        return L

    L = await query()
    return Response(
        {"id": L[0].id, "email": L[0].email, "c": L[1].count}, ResTypeEnum.JSON
    )


# test add data
@app.route("/test_db/add", allow_methods=["get"])
async def test_db_add(request: Request, person_args: P):
    async def add_one_person():
        new_person = Person.create(email=person_args.email)
        s = db.get_async_session()
        s.add(new_person)
        await db.Session.commit()
        return new_person

    p = await add_one_person()
    return Response({"id": p.id, "email": p.email}, ResTypeEnum.JSON)


if __name__ == "__main__":
    app.run(port=5001)
```

---

### json-rpc
```python
from simple_starlette import SimpleStarlette
from simple_starlette.rpc.json_rpc import JsonRpcServer

app = SimpleStarlette(__name__)

rpc_server = JsonRpcServer(app)


@rpc_server.register_rpc_method(name="ping")
def ping(name):
    return rpc_server.to_response(f"pong {name}")


if __name__ == "__main__":
    rpc_server.run(port=5001)

```

```python
from simple_starlette.rpc.json_rpc import JsonRpcClient

PingServer = JsonRpcClient(host='http://localhost:5001/', method="post", method_name='ping')
r = PingServer.get_response(params={"name": "jack"})

print(r.result)  # pong jack
```