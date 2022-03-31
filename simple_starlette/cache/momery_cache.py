# local memory
# Generally only applies to a stand-alone deployment
# -------------------------------------------------

import collections.abc
from typing import Any, OrderedDict, Union

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

class Cache(collections.abc.MutableMapping):
    """基于长度控的memory cahce
    基础封装类, 实现了基本的数据交互，长度控制
    """
        
    __slots__ = ["maxsize", "__current_size"]

    __size_map = _DefaultSize()
    
    __default_marker = object()
    
    def __init__(self, maxsize: int = 1000, getsizeof=None) -> None:
        if getsizeof:
            setattr(self,getsizeof,getsizeof)
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
    
    def put(self, name, value):
        # put item
        v_size = self.getsizeof(value)
        diffsize = v_size
        if name in self.cache_storage:
            if old_size:=self.__size_map[name] != v_size:
                diffsize = v_size - old_size
        else:
            if self.__current_size + v_size >= self.maxsize:
                raise CacheIsFull("attach max size")
        self.cache_storage[name] = value
        self.__size_map[name] = v_size
        self.__current_size += diffsize
    
    def pop(self, name, default=__default_marker):
        # pop item
        try:
            self.cache_storage.pop(name)
        except KeyError:
            if default is self.__default_marker:
                return self.__misskey__(name)
            return default
        size = self.__size_map.pop(name)
        self.__current_size -= size

    def check_in(self, name) -> bool:
        return name in self.cache_storage
                
    @staticmethod
    def getsizeof(_):
        # default getsizeof func
        return 1
    
    def __len__(self) -> int:
        return len(self.cache_storage)
    
    def __repr__(self):
        return "<Cache maxsize=%s, current_size=%s>" % (self.maxsize, self.__current_size)

    def __misskey__(self, key):
        raise KeyError(key)



class CustomLruCache(Cache):
    """
    Least Recently Used Cache
    """

    def __init__(self, maxsize: int):
        self.cache_storage = OrderedDict()
        self.maxsize = maxsize

    def make_key(self, args, kwargs) -> str:
        keys = args
        if kwargs:
            keys += (object(),)
            for _kw in kwargs.items():
                keys += _kw
        return hash(keys).__str__()

    def get(self, key: Union[int, str]):
        if key not in self.cache_storage:
            return None
        else:
            self.cache_storage.move_to_end(key)
            return self.cache_storage[key]

    def put(self, key: str, value: Any) -> None:
        self.cache_storage[key] = value
        self.cache_storage.move_to_end(key)
        if len(self.cache_storage) > self.maxsize:
            self.cache_storage.popitem(last=False)

    def all(self):
        return self.cache_storage.items()


def lru_cache_by_local_memory_decorator(
    maxsize: int = 1000,
    cache_none_result: bool = False,
    cache_none_result_expires: int = 60,
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
        cache_storage = CustomLruCache(maxsize)

        def wrapped(*args, **kwargs):
            key = cache_storage.make_key(args, kwargs)
            result = cache_storage.get(key)
            if result:
                return result
            result = func(*args, **kwargs)
            if result is None and not cache_none_result:
                return None
            cache_storage.put(key, result)
            return result

        return wrapped

    return decorator


class GlobalMemory(dict):
    """custom cache data to mem
    Some global variables, such as statistical data, the total line length, and so on
    """

    Ellipsis


local_g = GlobalMemory()
