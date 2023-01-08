from simple_starlette import (
    SimpleStarlette,
    Response,
    ResTypeEnum,
    Request,
)
from simple_starlette.middleware.rate_limiter import (
    RateLimiterMiddlewareGenFunc,
)

app = SimpleStarlette(
    __name__,
    middleware=[
        RateLimiterMiddlewareGenFunc(path="/", limit_count=2, rate_key="index_api")
    ],
)


@app.route("/")
class Index:
    async def get(self, request: Request):
        return Response({"ping": "pong"}, ResTypeEnum.JSON)


app.run()
