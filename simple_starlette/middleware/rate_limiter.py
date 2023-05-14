# rate_limit.py
# ------
import threading
from typing import Any, Callable, NewType, Optional, Type, TypeVar, cast

from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.types import ASGIApp, Receive, Scope, Send

from simple_starlette.cache.memory_cache import _TTLCache
from simple_starlette.db.redis import RedisClient
from simple_starlette.exceptions import OverLimitError, SimpleException
from simple_starlette.types import Route as _RouteT

from ..logger import getLogger
from . import MiddlewareAbs

logger = getLogger(__name__)

_ASGIAPP = NewType("_ASGIAPP", ASGIApp)
_Receive = NewType("_Receive", Receive)
_Send = NewType("_Send", Send)
_Scope = NewType("_Scope", Scope)


class RateLimiterMiddleWare(MiddlewareAbs):
    def __init__(self, app: _ASGIAPP, **options) -> None:
        self.app = app
        self.options = options
        self.cache_counter = _TTLCache(
            maxsize=-1, ttl=options["interval_time"]
        )
        self.cache_lock = _TTLCache(
            maxsize=-1, ttl=options["lock_expires"]
        )
        self.redis_client = cast(
            Optional[RedisClient], self.options.get("redis_client")
        )
        if self.redis_client:
            self._lock = self.redis_client.redis.lock(
                "rate_limit_lock_%s" % id(self),
                timeout=10,
                blocking_timeout=5,
            )
        else:
            self._lock = threading.Lock()

        super().__init__(app, **options)

    async def __call__(
        self, scope: _Scope, receive: _Receive, send: _Send
    ) -> Any:
        # rate_key count
        rate_key = self.options["rate_key"] or self.options.get(
            "rate_key_factory"
        )
    
        if callable(rate_key):
            request = Request(scope, receive, send)
            rate_key = rate_key(request)

        if not rate_key:
            rate_count_key = None
        else:
            rate_count_key = "rate_limit_%s_%s_count" % (
                self.options["path"],
                rate_key,
            )
        
        # rate_ley lock
        lock_key = "%s_lock" % (rate_key)

        # 判断路由，空值
        if self.options["path"] != scope["path"]:
            return await self.app(scope, receive, send)
        if not rate_count_key:
            return await self.app(scope, receive, send)

        # handle 
        with self._lock:
            if self.__check_is_overlimit(rate_count_key, lock_key, scope):
                raise self.options["exc_error"](
                    self.options["exc_error_msg"],
                    self.options["exc_error_code"],
                )

        await self.app(scope, receive, send)

    def __check_is_overlimit(self, rate_count_key, lock_key, scope):
        if scope["type"] == "lifespan":
            return

        # 判断限频锁
        if self.redis_client:
            is_lock = self.redis_client.redis.get(lock_key)
        else:
            is_lock = self.cache_lock.get(
                lock_key, raise_key_error=False
            )
        if is_lock:
            return True

        rate_count_key = cast(str,rate_count_key)
        # 获取计数
        if self.redis_client:
            count = int(
                self.redis_client.redis.get(rate_count_key) or 0
            )
        else:
            count = int(
                self.cache_counter.get(
                    rate_count_key, raise_key_error=False
                )
                or 0
            )

        # 判断是否超过限制
        if count >= self.options["limit_count"]:
            if self.redis_client:
                self.redis_client.redis.set(
                    lock_key, 1, ex=self.options["lock_expires"]
                )
                self.redis_client.redis.delete(rate_count_key)
            else:
                self.cache_lock.set(lock_key, True)
                self.cache_counter.pop(rate_count_key)
            return True

        # ++计数
        if self.redis_client:
            res = self.redis_client.redis.incr(rate_count_key)
            if res == 1:
                self.redis_client.redis.expire(
                    rate_count_key, self.options["interval_time"]
                )
        else:
            self.cache_counter.set(rate_count_key, count + 1)

        return False


R = TypeVar("R", bound=_RouteT)


def rate_limit(
    app,
    route: R = None,
    interval_time: int = 60,
    limit_count: int = 100,
    lock_expires: int = 10,
    rate_key: Optional[str] = None,
    redis_client: Optional[RedisClient] = None,
    rate_key_factory: Optional[Callable] = None,
    exc_error: Optional[Type[SimpleException]] = OverLimitError,
    exc_error_msg: str = "api请求数到达限制",
    exc_error_code: int = 406,
) -> R:  # type: ignore
    options = {}
    assert (
        rate_key or rate_key_factory
    ), "rate_key， rate_key_factory不能都为空"
    options["app"] = app
    options["exc_error"] = exc_error
    options["exc_error_msg"] = exc_error_msg
    options["exc_error_code"] = exc_error_code
    options["interval_time"] = interval_time
    options["rate_key"] = rate_key
    options["limit_count"] = limit_count
    options["redis_client"] = redis_client
    options["lock_expires"] = lock_expires + interval_time
    options["rate_key_factory"] = rate_key_factory
    if not route:
        return lambda route: rate_limit(route=route, **options)  # type: ignore
    options["path"] = route.path

    options.pop("app", 0)
    app.middleware.append(
        Middleware(RateLimiterMiddleWare, **options)
    )


def RateLimiterMiddlewareGenFunc(
    route: _RouteT,
    interval_time: int = 60,
    limit_count: int = 100,
    lock_expires: int = 10,
    rate_key: Optional[str] = None,
    redis_client: Optional[RedisClient] = None,
    rate_key_factory: Optional[Callable] = None,
    exc_error: Optional[Type[SimpleException]] = OverLimitError,
    exc_error_msg: str = "api请求数到达限制",
    exc_error_code: int = 406,
) -> Middleware:
    """
    :redis_client 使用分布式整体限制频率，需要指定一个redis服务端
    :rate_key 限频key值
    :rate_key_factory 限频key值工厂函数
    """
    options = {}
    assert (
        rate_key or rate_key_factory
    ), "rate_key， rate_key_factory不能都为空"
    options["exc_error"] = exc_error
    options["exc_error_msg"] = exc_error_msg
    options["exc_error_code"] = exc_error_code
    options["interval_time"] = interval_time
    options["rate_key"] = rate_key
    options["limit_count"] = limit_count
    options["redis_client"] = redis_client
    options["lock_expires"] = lock_expires + interval_time
    options["rate_key_factory"] = rate_key_factory
    options["path"] = route.path
    return Middleware(RateLimiterMiddleWare, **options)
