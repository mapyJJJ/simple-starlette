"""
This type stub file was generated by pyright.
"""

import greenlet
from typing import Any, Callable, Coroutine

def is_exit_exception(e: Any):
    ...

class _AsyncIoGreenlet(greenlet.greenlet):
    driver: Any = ...
    gr_context: Any = ...
    def __init__(self, fn: Any, driver: Any) -> None:
        ...
    


def await_only(awaitable: Coroutine) -> Any:
    ...

def await_fallback(awaitable: Coroutine) -> Any:
    ...

async def greenlet_spawn(fn: Callable, *args: Any, _require_await: Any = ..., **kwargs: Any) -> Any:
    ...

class AsyncAdaptedLock:
    def mutex(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, *arg: Any, **kw: Any) -> None:
        ...
    


def get_event_loop():
    ...

