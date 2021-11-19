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

### cbv
```python
@app.route("/test")
class Test:
    async def get(self, request: Request):
        return Response(request.url, ResTypeEnum.TEXT)

    async def post(self, request: Request):
        return Response(request.url, ResTypeEnum.TEXT)
```

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