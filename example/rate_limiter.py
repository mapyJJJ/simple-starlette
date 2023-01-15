from simple_starlette import (
    SimpleStarlette,
    Response,
    ResTypeEnum,
    Request,
)
from simple_starlette.args import QueryParams
from simple_starlette.middleware.rate_limiter import (
    RateLimiterMiddlewareGenFunc,
    rate_limit,
)
from simple_starlette.db.redis import RedisClient
from simple_starlette import request
from simple_starlette.logger import getLogger

logger = getLogger(__name__)

app = SimpleStarlette(__name__)
redis_client = RedisClient(app, "127.0.0.1", 6379, 0)


@rate_limit(app, rate_key="index_api", limit_count=2)  # 使用语法糖
@app.route("/")
class Index:
    async def get(self, request: Request):
        return Response({"ping": "pong"}, ResTypeEnum.JSON)


@app.route("/test")
class IndexTest:
    async def get(self, request: Request):
        return Response({"ping": "pong"}, ResTypeEnum.JSON)


@rate_limit(
    app,
    redis_client=redis_client,
    limit_count=1,
    rate_key="index_test_m",
)  # 使用redis，实现分布式控制
@app.route("/test/m")
class IndexTestM:
    async def get(self, request: Request):
        return Response({"ping": "pong"}, ResTypeEnum.JSON)


# 自行注册
app.middleware.append(
    RateLimiterMiddlewareGenFunc(
        route=IndexTest, limit_count=4, rate_key="index_test_api"
    )
)

# 此处演示的例子是针对全局api的限频，但大部分情况是需要结合业务来限制频率，
# 如针对每个用户来进行api限频，可以根据 通过 rate_key_factory 实现
# 如下:
def user_info_rate_limit_gen(_request: Request):
    if _request.query_params.get("user_id"):
        rate_key = "user_info_%s" % _request.query_params["user_id"]
        return rate_key
    return None


@rate_limit(app, rate_key_factory=user_info_rate_limit_gen,limit_count=5)
@app.route("/user/info")
class UserInfo:
    class Query(QueryParams):
        user_id: int

    async def get(self, request: Request, q: Query):
        return Response({"user_id": q.user_id}, ResTypeEnum.JSON)

if __name__ == "__main__":
    app.run()
