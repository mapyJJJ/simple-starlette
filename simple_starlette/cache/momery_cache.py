# local memory
# Generally only applies to a stand-alone deployment
# -------------------------------------------------

import time
from abc import ABCMeta
from functools import singledispatch
from types import FunctionType
from typing import Any, Callable, OrderedDict, Union


class CacheIsFull(Exception):
    Ellipsis


class _DefaultSize:

    __slots__ = ()

    def __getitem__(self, _):
        return 1

    def __setitem__(self, _, value):
        assert value == 1

    def pop(self, _):
        return 1


class Cache(metaclass=ABCMeta):
    """
    cache 抽象类
    """

    __size_map = _DefaultSize()

    _default_marker = object()

    def __init__(self, maxsize: int = 1000, getsizeof=None) -> None:
        if getsizeof:
            setattr(self, "getsizeof", getsizeof)
        if self.getsizeof is not Cache.getsizeof:
            self.__size_map = dict()
        self.maxsize = maxsize
        self.cache_storage = {}
        self.__current_size = 0

    def make_key(self, *args, **kwargs) -> str:
        # gen cache key
        keys = args
        if kwargs:
            keys += (object(),)
            for _kw in kwargs.items():
                keys += _kw
        return hash(keys).__str__()

    def get(self, name):
        try:
            return self.cache_storage[name]
        except KeyError:
            return self.__misskey__(name)

    def set(self, name, value):
        # put item
        v_size = self.getsizeof(value)
        diffsize = v_size
        if name in self.cache_storage:
            if old_size := self.__size_map[name] != v_size:
                diffsize = v_size - old_size
        else:
            if self.__current_size + v_size > self.maxsize:
                raise CacheIsFull("attach max size")
        self.cache_storage[name] = value
        self.__size_map[name] = v_size
        self.__current_size += diffsize

    def pop(self, name, default=_default_marker):
        # pop item
        try:
            self.cache_storage.pop(name)
        except KeyError:
            if default is self._default_marker:
                return self.__misskey__(name)
            return default
        size = self.__size_map.pop(name)
        self.__current_size -= size

    def check_in(self, name) -> bool:
        return name in self.cache_storage

    @property
    def size(self):
        return self.__current_size

    @staticmethod
    def getsizeof(_):
        # default getsizeof func
        return 1

    def __len__(self) -> int:
        return len(self.cache_storage)

    def __repr__(self):
        return "<Cache maxsize=%s, current_size=%s>" % (
            self.maxsize,
            self.__current_size,
        )

    def __misskey__(self, key):
        raise KeyError(key)


class _Timer:
    """
    timer ctx
    """

    def __init__(self, point_time_func: Callable) -> None:
        self.point_time_func = point_time_func
        self.__time_flag = 0

    def __enter__(self):
        if self.__time_flag == 0:
            self.__time_point = self.point_time_func()
        self.__time_flag += 1
        return self.__time_point

    def __exit__(self, *exc):
        self.__time_flag -= 1

    def __call__(self):
        if self.__time_flag == 0:
            return self.point_time_func()
        return self.__time_point


class _TimerCache(Cache):
    def __init__(
        self,
        maxsize: int,
        getsizeof=None,
        point_time_func=time.monotonic,
    ) -> None:
        super().__init__(maxsize=maxsize, getsizeof=getsizeof)
        self.__timer = _Timer(point_time_func)
        self.__time_map = {}

    def get(self, name):
        with self.__timer as _t:
            expired = False
            try:
                if _t > self.__time_map[name]:
                    expired = True
            except KeyError:
                expired = False
            if expired:
                self.expire_key(name)
                return self.__misskey__(name)
            else:
                return super().get(name)

    def default_expire_at(self, s: int):
        return self.__timer() + s

    def set(self, expire_at_factory, name, value):
        @singledispatch
        def _set(expire_at_factory):
            Ellipsis

        @_set.register
        def _(expire_at_factory: int):
            print(name, value)
            super(_TimerCache, self).set(name, value)
            self.__time_map[name] = self.default_expire_at(
                expire_at_factory
            )

        @_set.register
        def _(expire_at_factory: FunctionType):
            super().set(name, value)
            expire_at = expire_at_factory()
            self.__time_map[name] = expire_at

        return _set(expire_at_factory)

    def pop(self, name, default=None):
        if not default:
            default = self._default_marker
        super().pop(name, default)
        self.expire_key(name)

    def expire_key(self, name):
        self.__time_map.pop(name, 0)
        super().pop(name, 0)


class _TTLCache(_TimerCache):
    def __init__(
        self,
        maxsize: int,
        ttl: int,
        getsizeof=Cache.getsizeof,
        point_time_func=time.monotonic,
    ) -> None:
        super().__init__(
            maxsize,
            getsizeof=getsizeof,
            point_time_func=point_time_func,
        )
        self._ttl = ttl

    def set(self, name, value):
        super().set(
            expire_at_factory=self._ttl, name=name, value=value
        )

    def get(self, name, raise_key_error: bool = True):
        try:
            return super().get(name)
        except KeyError as e:
            if raise_key_error:
                raise e
        return None

    def pop(self, name):
        super().pop(name)


class LruCache(_TTLCache):
    """
    Least Recently Used Cache
    """

    def __init__(self, maxsize: int, ttl: int):
        super().__init__(maxsize=maxsize, ttl=ttl)
        self.cache_storage = OrderedDict()

    def get(
        self, key: Union[int, str], raise_key_error: bool = False
    ):
        v = None
        try:
            v = super().get(key)
        except KeyError as e:
            if raise_key_error:
                raise e
        if v:
            self.cache_storage.move_to_end(key)
        return v

    def set(self, key: str, value: Any) -> None:
        if self.size >= self.maxsize:
            k = next(iter(self.cache_storage))
            super().pop(k)
        super().set(key, value)
        self.cache_storage.move_to_end(key)

    def all(self):
        return self.cache_storage.items()


def lru_cache_decorator(
    maxsize: int = 1000,
    cache_none_result: bool = False,
    cache_ttl: int = 30 * 60 * 60,
):
    """cache on local

    maxsize: Maximum number of hotspots section of the data, Need to think about memory leaks, reasonable setting

    Back to the null:
        cache_none_result: cache none result ?
        cache_none_result_expires: cache none expires


    Usage Example:
        @lru_cache_by_local_memory_decorator()
        def calc_func(x, y, ...):
            ...
            return result
    """

    def decorator(func):
        cache_storage = LruCache(maxsize, cache_ttl)

        def wrapped(*args, **kwargs):
            key = cache_storage.make_key(*args, **kwargs)
            result = cache_storage.get(key)
            if result:
                return result
            result = func(*args, **kwargs)
            if result is None and not cache_none_result:
                return None
            cache_storage.set(key, result)
            return result

        return wrapped

    return decorator


class GlobalMemory(dict):
    """
    存放一些全局通用的变量，如：访问计数，server启动时间等，业务相关，请使用上面的缓存方法
    """

    Ellipsis


local_g = GlobalMemory()
