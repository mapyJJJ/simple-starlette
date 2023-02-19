import sys
from typing import Optional

import redis
from redis import ConnectionPool, Redis

from ..logger import getLogger

logger = getLogger(__name__)


class RedisCommonConfig:
    db: int = 0


class RedisClient:
    def __init__(
        self,
        app,
        redis_db_uri: str = "",
        redis_port: Optional[int] = None,
        db: int = 0,
    ) -> None:
        db_uri = redis_db_uri or app.config.get("REDIS_DB_URI", None)
        if not db_uri:
            raise AttributeError(
                "init redis db , the `REDIS_DB_URI` must be set"
            )
        pool = ConnectionPool(host=db_uri, port=redis_port, db=db)
        self.redis = Redis(connection_pool=pool)
        self.redis.info()

        self.__check_connection()

    def __check_connection(self):
        try:
            self.redis.info()
        except redis.exceptions.ConnectionError:
            logger.error("连接redis失败,检查配置，以及确保服务可被访问")
            sys.exit(0)
