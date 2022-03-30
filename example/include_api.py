from simple_starlette.responses import ResTypeEnum, Response
from requests.sessions import Request
from simple_starlette.include import Include
from simple_starlette import SimpleStarlette

app = SimpleStarlette(__name__)

api = Include(app, '/api')

@api.route("/index")
class Index:
    def get(self, request: Request):
        return Response({"url": str(request.url)}, ResTypeEnum.JSON)


app.run()