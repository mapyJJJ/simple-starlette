from time import sleep
from simple_starlette.cache.momery_cache import lru_cache_decorator

def test_lru():
    c = 0

    @lru_cache_decorator(cache_ttl=3)
    def res(x, y):
        if c not in (0, 2):
            raise AssertionError()
        if c == 2:
            return x*y
        return x+y

    res(1,2)
    c += 1
    res(1,2)
    sleep(3)
    c += 1
    assert res(1,2) == 2


