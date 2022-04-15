# redis_cache.py
# common cache case
# --------------------

from typing import TYPE_CHECKING, Any

from redis import ConnectionPool
from redis import Redis as _Redis

if TYPE_CHECKING:

    class Redis(_Redis):
        def __init__(
            self,
            host,
            port,
            db,
            password,
            max_connections: int = 10000,
        ) -> None:
            ...

else:

    class Redis:
        def __init__(
            self,
            host,
            port,
            db,
            password,
            max_connections: int = 10000,
        ) -> None:
            self._redis = _Redis(
                connection_pool=ConnectionPool(
                    host=host, port=port, db=db, password=password
                ),
                max_connections=max_connections,
            )
