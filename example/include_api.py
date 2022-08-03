# --Include--
# 路由分级

from simple_starlette import SimpleStarlette, Request
from simple_starlette.include import Include
from simple_starlette.responses import Response, ResTypeEnum

app = SimpleStarlette(__name__)

api = Include(app, "/api")
admin_api = Include(app, "/admin/api")

@api.route("/index")  # /api/index
class Index:
    def get(self, request: Request):
        return Response({"url": str(request.url)}, ResTypeEnum.JSON)


@admin_api.route("/index") # /admin/api/index
class AdminIndex:
    def get(self, request: Request):
        return Response({"url": str(request.url)}, ResTypeEnum.JSON)


if __name__ == "__main__":
    app.run()
