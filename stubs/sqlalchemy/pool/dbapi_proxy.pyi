from .. import util as util
from ..util import threading as threading
from .impl import QueuePool as QueuePool
from typing import Any

proxies: Any

def manage(module: Any, **params: Any): ...
def clear_managers() -> None: ...

class _DBProxy:
    module: Any = ...
    kw: Any = ...
    poolclass: Any = ...
    pools: Any = ...
    def __init__(self, module: Any, poolclass: Any = ..., **kw: Any) -> None: ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
    def __getattr__(self, key: Any): ...
    def get_pool(self, *args: Any, **kw: Any): ...
    def connect(self, *args: Any, **kw: Any): ...
    def dispose(self, *args: Any, **kw: Any) -> None: ...
