# Simple-Starlette

### simple example
```python
from starlette.requests import Request
from simple_starlette import SimpleStarlette, Response, ResTypeEnum

app = SimpleStarlette(__name__)


@app.route("/test")
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