# local memory
# Generally only applies to a stand-alone deployment
# -------------------------------------------------

from typing import Any, OrderedDict, Union


class CustomLruCache:
    """
    use OrderedDict realize strategy like lru
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


def cache_by_local_memory_decorator(
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
        @cache_by_local_memory()
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
