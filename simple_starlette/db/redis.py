from redis import ConnectionPool, Redis


class RedisCommonConfig:
    db: int = 0


class RedisClient:
    def __init__(
        self,
        app,
        redis_db_uri: str = "",
        redis_port: int = None,
        db: int = 0,
    ) -> None:
        db_uri = redis_db_uri or app.config.get("REDIS_DB_URI", None)
        if not db_uri:
            raise AttributeError(
                "init redis db , the `REDIS_DB_URI` must be set"
            )
        pool = ConnectionPool(host=db_uri, port=redis_port, db=db)
        self.redis = Redis(connection_pool=pool)
