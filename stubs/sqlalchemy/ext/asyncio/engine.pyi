from ... import exc as exc, inspection as inspection, util as util
from ...engine.base import NestedTransaction as NestedTransaction
from ...future import Connection as Connection, Engine as Engine
from ...util.concurrency import greenlet_spawn as greenlet_spawn
from .base import ProxyComparable as ProxyComparable, StartableContext as StartableContext
from .result import AsyncResult as AsyncResult
from typing import Any, Optional

def create_async_engine(*arg: Any, **kw: Any): ...

class AsyncConnectable: ...

class AsyncConnection(ProxyComparable, StartableContext, AsyncConnectable):
    engine: Any = ...
    sync_engine: Any = ...
    sync_connection: Any = ...
    def __init__(self, async_engine: Any, sync_connection: Optional[Any] = ...) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    @property
    def connection(self) -> None: ...
    async def get_raw_connection(self): ...
    @property
    def info(self): ...
    def begin(self): ...
    def begin_nested(self): ...
    async def invalidate(self, exception: Optional[Any] = ...): ...
    async def get_isolation_level(self): ...
    async def set_isolation_level(self): ...
    def in_transaction(self): ...
    def in_nested_transaction(self): ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    async def execution_options(self, **opt: Any): ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
    async def close(self) -> None: ...
    async def exec_driver_sql(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Any = ...): ...
    async def stream(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Any = ...): ...
    async def execute(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Any = ...): ...
    async def scalar(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Any = ...): ...
    async def scalars(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Any = ...): ...
    async def stream_scalars(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Any = ...): ...
    async def run_sync(self, fn: Any, *arg: Any, **kw: Any): ...
    def __await__(self): ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class AsyncEngine(ProxyComparable, AsyncConnectable):
    class _trans_ctx(StartableContext):
        conn: Any = ...
        def __init__(self, conn: Any) -> None: ...
        transaction: Any = ...
        async def start(self, is_ctxmanager: bool = ...): ...
        async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    sync_engine: Any = ...
    def __init__(self, sync_engine: Any) -> None: ...
    def begin(self): ...
    def connect(self): ...
    async def raw_connection(self): ...
    def execution_options(self, **opt: Any): ...
    async def dispose(self): ...

class AsyncTransaction(ProxyComparable, StartableContext):
    connection: Any = ...
    sync_transaction: Any = ...
    nested: Any = ...
    def __init__(self, connection: Any, nested: bool = ...) -> None: ...
    @property
    def is_valid(self): ...
    @property
    def is_active(self): ...
    async def close(self) -> None: ...
    async def rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...