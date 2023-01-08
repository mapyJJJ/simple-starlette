from simple_starlette import (
    SimpleStarlette,
    Response,
    ResTypeEnum,
    Request,
)
from simple_starlette.middleware.rate_limiter import (
    RateLimiterMiddlewareGenFunc,
)


app = SimpleStarlette(__name__)

@app.route("/")
class Index:
    async def get(self, request: Request):
        return Response({"ping": "pong"}, ResTypeEnum.JSON)

@app.route("/test")
class IndexTest:
    async def get(self, request: Request):
        return Response({"ping": "pong"}, ResTypeEnum.JSON)


app.middleware.append(RateLimiterMiddlewareGenFunc(path="/", limit_count=2, rate_key="index_api"))
app.middleware.append(RateLimiterMiddlewareGenFunc(IndexTest, limit_count=4, rate_key="index_api"))
if __name__ == "__main__":
    app.run()
