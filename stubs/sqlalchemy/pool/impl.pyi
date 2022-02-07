from .. import exc as exc, util as util
from ..util import chop_traceback as chop_traceback, threading as threading
from .base import Pool as Pool
from typing import Any

class QueuePool(Pool):
    def __init__(self, creator: Any, pool_size: int = ..., max_overflow: int = ..., timeout: float = ..., use_lifo: bool = ..., **kw: Any) -> None: ...
    def recreate(self): ...
    def dispose(self) -> None: ...
    def status(self): ...
    def size(self): ...
    def timeout(self): ...
    def checkedin(self): ...
    def overflow(self): ...
    def checkedout(self): ...

class AsyncAdaptedQueuePool(QueuePool): ...
class FallbackAsyncAdaptedQueuePool(AsyncAdaptedQueuePool): ...

class NullPool(Pool):
    def status(self): ...
    def recreate(self): ...
    def dispose(self) -> None: ...

class SingletonThreadPool(Pool):
    size: Any = ...
    def __init__(self, creator: Any, pool_size: int = ..., **kw: Any) -> None: ...
    def recreate(self): ...
    def dispose(self) -> None: ...
    def status(self): ...
    def connect(self): ...

class StaticPool(Pool):
    def connection(self): ...
    def status(self): ...
    def dispose(self) -> None: ...
    def recreate(self): ...

class AssertionPool(Pool):
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    def status(self): ...
    def dispose(self) -> None: ...
    def recreate(self): ...