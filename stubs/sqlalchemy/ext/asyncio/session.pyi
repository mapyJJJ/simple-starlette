from . import engine as engine
from ... import util as util
from ...orm import Session as Session, object_session as object_session
from ...util.concurrency import greenlet_spawn as greenlet_spawn
from .base import ReversibleProxy as ReversibleProxy, StartableContext as StartableContext
from typing import Any, Optional

class AsyncSession(ReversibleProxy):
    dispatch: Any = ...
    bind: Any = ...
    binds: Any = ...
    sync_session_class: Any = ...
    sync_session: Any = ...
    def __init__(self, bind: Optional[Any] = ..., binds: Optional[Any] = ..., sync_session_class: Optional[Any] = ..., **kw: Any) -> None: ...
    async def refresh(self, instance: Any, attribute_names: Optional[Any] = ..., with_for_update: Optional[Any] = ...): ...
    async def run_sync(self, fn: Any, *arg: Any, **kw: Any): ...
    async def execute(self, statement: Any, params: Optional[Any] = ..., execution_options: Any = ..., bind_arguments: Optional[Any] = ..., **kw: Any): ...
    async def scalar(self, statement: Any, params: Optional[Any] = ..., execution_options: Any = ..., bind_arguments: Optional[Any] = ..., **kw: Any): ...
    async def scalars(self, statement: Any, params: Optional[Any] = ..., execution_options: Any = ..., bind_arguments: Optional[Any] = ..., **kw: Any): ...
    async def get(self, entity: Any, ident: Any, options: Optional[Any] = ..., populate_existing: bool = ..., with_for_update: Optional[Any] = ..., identity_token: Optional[Any] = ...): ...
    async def stream(self, statement: Any, params: Optional[Any] = ..., execution_options: Any = ..., bind_arguments: Optional[Any] = ..., **kw: Any): ...
    async def stream_scalars(self, statement: Any, params: Optional[Any] = ..., execution_options: Any = ..., bind_arguments: Optional[Any] = ..., **kw: Any): ...
    async def delete(self, instance: Any): ...
    async def merge(self, instance: Any, load: bool = ..., options: Optional[Any] = ...): ...
    async def flush(self, objects: Optional[Any] = ...) -> None: ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    async def connection(self, **kw: Any): ...
    def begin(self, **kw: Any): ...
    def begin_nested(self, **kw: Any): ...
    async def rollback(self): ...
    async def commit(self): ...
    async def close(self): ...
    @classmethod
    async def close_all(self): ...
    async def __aenter__(self): ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class _AsyncSessionContextManager:
    async_session: Any = ...
    def __init__(self, async_session: Any) -> None: ...
    trans: Any = ...
    async def __aenter__(self): ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

class AsyncSessionTransaction(ReversibleProxy, StartableContext):
    session: Any = ...
    nested: Any = ...
    sync_transaction: Any = ...
    def __init__(self, session: Any, nested: bool = ...) -> None: ...
    @property
    def is_active(self): ...
    async def rollback(self) -> None: ...
    async def commit(self) -> None: ...
    async def start(self, is_ctxmanager: bool = ...): ...
    async def __aexit__(self, type_: Any, value: Any, traceback: Any) -> None: ...

def async_object_session(instance: Any): ...
def async_session(session: Any): ...