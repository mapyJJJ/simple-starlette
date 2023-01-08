from simple_starlette import SimpleStarlette, QueryParams, Request, ResTypeEnum, Response
from simple_starlette.db.redis import RedisClient
from simple_starlette.logger import getLogger

logger = getLogger(__name__)
app = SimpleStarlette(__name__)

redis = RedisClient(app, redis_db_uri="localhost", redis_port=6379, db=0).redis

@app.route("/index")
class Index:
    # 定义 get 方法
    async def get(self, request: Request):
        res = redis.incr("test")
        return Response({"test": res}, ResTypeEnum.JSON)

app.run()