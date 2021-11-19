import pydantic
from starlette.requests import Request

from simple_starlette import Include, Response, ResTypeEnum, SimpleStarlette
from simple_starlette.args import BaseModel, register_args

app = SimpleStarlette("__name__")

# response


@app.route("/return_json")
async def ping(request):
    return Response({"res": "pong"}, ResTypeEnum.JSON)


@app.route("/return_text")
async def ping(request):
    return Response("pong", ResTypeEnum.TEXT)


@app.route("/return_html")
async def ping(request):
    return Response("<h1>pong</h1>", ResTypeEnum.HTML)


# cbv
@app.route("/cbv_1")
class Cbv1:
    class GetArgs(pydantic.BaseModel):
        name: str

    async def get(self, request, args: GetArgs):
        return Response(f"get, {args.name}", ResTypeEnum.TEXT)

    async def post(self, request):
        return Response("post", ResTypeEnum.TEXT)


# fbv
@register_args
class GetArgs(BaseModel):
    name: str


@app.route("/fbv_1")
def get_args(request, args: GetArgs):
    return Response(f"get, {args.name}", ResTypeEnum.TEXT)


from simple_starlette import g


def set_to_global(i):
    g.res = i


def get_from_global():
    return g.res


async def get_from_global_2():
    import asyncio

    await asyncio.sleep(10)
    return g.res


# include
api = Include(app, "/api")


@api.route("/ping1")
async def ping1(request):
    set_to_global(1)
    get_from_global()
    return Response(str(get_from_global()), ResTypeEnum.TEXT)


@api.route("/ping2")
async def ping1(request):
    set_to_global(2)
    res = await get_from_global_2()
    return Response(str(res), ResTypeEnum.TEXT)


from starlette.requests import Request
from simple_starlette import SimpleStarlette, Response, ResTypeEnum

app = SimpleStarlette(__name__)


from simple_starlette import BaseModel, register_args

@register_args
class GetArgs(BaseModel):
    name: str

@app.route("/test")
async def test(self, request: Request, params1: GetArgs):
    return Response(params1.name, ResTypeEnum.TEXT)

app.run()
