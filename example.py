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
    GetArgs.validate({})
    async def get(self, request, args: GetArgs):
        return Response(f"get, {args.name}", ResTypeEnum.TEXT)

    async def post(self, request):
        return Response("post", ResTypeEnum.TEXT)



app.run()
