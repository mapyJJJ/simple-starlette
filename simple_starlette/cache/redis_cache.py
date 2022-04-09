# redis_cache.py
# common cache case
# --------------------

from redis import ConnectionPool, Redis


class _Redis:
    def __init__(self, host, port, db, password) -> None:
        self._redis = Redis(
            connection_pool=ConnectionPool(
                host=host, port=port, db=db, password=password
            ),
            max_connections=10000,
        )
