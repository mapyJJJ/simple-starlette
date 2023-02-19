from time import sleep
from simple_starlette.cache.memory_cache import lru_cache_decorator

def test_lru():
    execute_add_count = 0

    @lru_cache_decorator(cache_ttl=3)
    def add(x,y):
        nonlocal execute_add_count
        execute_add_count += 1
        return x+y

    res = add(1,1)
    assert (res == 2 and execute_add_count == 1)
    res = add(1,1)
    assert (res == 2 and execute_add_count == 1)
    sleep(3)
    res = add(1,1)
    assert (res == 2 and execute_add_count == 2)
