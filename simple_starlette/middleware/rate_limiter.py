# rate_limit.py
# ------
from typing import Any, Callable, Optional

import redis
from starlette.middleware import Middleware
from starlette.types import ASGIApp, Receive, Scope, Send

from simple_starlette.db.redis import RedisClient

from . import MiddlewareAbs


class RateLimiterMiddleWare(MiddlewareAbs):
    def __init__(self, app: ASGIApp, **options) -> None:
        super().__init__(app, **options)

    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> Any:
        return await super().__call__(scope, receive, send)


def RateLimiterMiddlewareGenFunc(
    expires: int = 60,
    limit_count: int = 100,
    rate_key: str = "default-limiter-key",
    redis_client: Optional[RedisClient] = None,
    rate_key_factory: Optional[Callable] = None,
):
    """
    :redis_client 使用分布式整体限制频率，需要指定一个redis
    :rate_key 限频key值
    :rate_key_factory 限频key值工厂函数
    """

    options = {}
    if redis_client:
        try:
            redis_client.redis.client_info()
        except redis.exceptions.ConnectionError:
            pass
    options["expires"] = expires
    options["rate_key"] = rate_key
    options["limit_count"] = limit_count
    options["redis_client"] = redis_client
    options["rate_key_factory"] = rate_key_factory
    return Middleware(RateLimiterMiddleWare, **options)
