# rate_limit.py
# ------
from typing import Any, Callable, Optional, Type
from starlette.middleware import Middleware
from starlette.types import ASGIApp, Receive, Scope, Send
from simple_starlette.cache.memory_cache import _TTLCache
from simple_starlette.db.redis import RedisClient
from simple_starlette.exceptions import (
    SimpleException,
    OverLimitError,
)
from . import MiddlewareAbs

from ..logger import getLogger

logger = getLogger(__name__)


class RateLimiterMiddleWare(MiddlewareAbs):
    def __init__(self, app: ASGIApp, **options) -> None:
        self.app = app
        self.options = options
        self.cache_counter = _TTLCache(
            maxsize=-1, ttl=options["expires"]
        )
        self.cache_lock = _TTLCache(
            maxsize=-1, ttl=options["lock_expires"]
        )
        super().__init__(app, **options)

    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> Any:
        if self.options["path"] != scope["path"]:
            await self.app(scope, receive, send)
    
        if self.__check_is_overlimit(scope):
            raise self.options["exc_error"](
                self.options["exc_error_msg"],
                self.options["exc_error_code"]
            )
        await self.app(scope, receive, send)

    def __check_is_overlimit(self, scope):
        if scope["type"] == "lifespan":
            return
        rate_key = self.options["rate_key"] or self.options.get(
            "rate_key_factory"
        )
        rate_key = self.options["path"] + "|" + rate_key

        is_lock = self.cache_lock.get(rate_key, raise_key_error=False)
        if is_lock:
            return True

        count = (
            self.cache_counter.get(rate_key, raise_key_error=False)
            or 0
        )
        if count >= self.options["limit_count"]:
            self.cache_lock.set(rate_key, True)
            self.cache_counter.pop(rate_key)
            return True
        self.cache_counter.set(rate_key, count + 1)
        return False


def RateLimiterMiddlewareGenFunc(
    path: str = "/",
    expires: int = 60,
    limit_count: int = 100,
    lock_expires: int = 10,
    rate_key: Optional[str] = None,
    redis_client: Optional[RedisClient] = None,
    rate_key_factory: Optional[Callable] = None,
    exc_error: Optional[Type[SimpleException]] = OverLimitError,
    exc_error_msg: str = "api请求数到达限制",
    exc_error_code: int = 406,
):
    """
    :redis_client 使用分布式整体限制频率，需要指定一个redis
    :rate_key 限频key值
    :rate_key_factory 限频key值工厂函数
    """

    options = {}
    assert (
        rate_key or rate_key_factory
    ), "rate_key， rate_key_factory不能都为空"
    options["path"] = path
    options["exc_error"] = exc_error
    options["exc_error_msg"] = exc_error_msg
    options["exc_error_code"] = exc_error_code
    options["expires"] = expires
    options["rate_key"] = rate_key
    options["limit_count"] = limit_count
    options["redis_client"] = redis_client
    options["lock_expires"] = lock_expires
    options["rate_key_factory"] = rate_key_factory
    return Middleware(RateLimiterMiddleWare, **options)
