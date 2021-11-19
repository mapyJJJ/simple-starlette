from simple_starlette.args import BaseModel, register_args
from simple_starlette import Include
import pydantic
from simple_starlette import SimpleStarlette, ResTypeEnum, Response

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


# include
api = Include(app, "/api")


@api.route("/ping1")
async def ping1(request):
    return Response("pong1", ResTypeEnum.TEXT)


app.run()
