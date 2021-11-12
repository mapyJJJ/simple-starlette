from .. import exc as exc, inspection as inspection, log as log, util as util
from ..sql import compiler as compiler
from .interfaces import Connectable as Connectable, ExceptionContext as ExceptionContext
from .util import TransactionalContext as TransactionalContext
from typing import Any, Optional

class Connection(Connectable):
    engine: Any = ...
    dialect: Any = ...
    should_close_with_result: bool = ...
    dispatch: Any = ...
    def __init__(self, engine: Any, connection: Optional[Any] = ..., close_with_result: bool = ..., _branch_from: Optional[Any] = ..., _execution_options: Optional[Any] = ..., _dispatch: Optional[Any] = ..., _has_events: Optional[Any] = ..., _allow_revalidate: bool = ...) -> None: ...
    def schema_for_object(self, obj: Any): ...
    def __enter__(self): ...
    def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def execution_options(self, **opt: Any): ...
    def get_execution_options(self): ...
    @property
    def closed(self): ...
    @property
    def invalidated(self): ...
    @property
    def connection(self): ...
    def get_isolation_level(self): ...
    @property
    def default_isolation_level(self): ...
    @property
    def info(self): ...
    def connect(self, close_with_result: bool = ...): ...
    def invalidate(self, exception: Optional[Any] = ...): ...
    def detach(self) -> None: ...
    def begin(self): ...
    def begin_nested(self): ...
    def begin_twophase(self, xid: Optional[Any] = ...): ...
    def recover_twophase(self): ...
    def rollback_prepared(self, xid: Any, recover: bool = ...) -> None: ...
    def commit_prepared(self, xid: Any, recover: bool = ...) -> None: ...
    def in_transaction(self): ...
    def in_nested_transaction(self): ...
    def get_transaction(self): ...
    def get_nested_transaction(self): ...
    def close(self) -> None: ...
    def scalar(self, object_: Any, *multiparams: Any, **params: Any): ...
    def scalars(self, object_: Any, *multiparams: Any, **params: Any): ...
    def execute(self, statement: Any, *multiparams: Any, **params: Any): ...
    def exec_driver_sql(self, statement: Any, parameters: Optional[Any] = ..., execution_options: Optional[Any] = ...): ...
    def transaction(self, callable_: Any, *args: Any, **kwargs: Any): ...
    def run_callable(self, callable_: Any, *args: Any, **kwargs: Any): ...

class ExceptionContextImpl(ExceptionContext):
    engine: Any = ...
    connection: Any = ...
    sqlalchemy_exception: Any = ...
    original_exception: Any = ...
    execution_context: Any = ...
    statement: Any = ...
    parameters: Any = ...
    is_disconnect: Any = ...
    invalidate_pool_on_disconnect: Any = ...
    def __init__(self, exception: Any, sqlalchemy_exception: Any, engine: Any, connection: Any, cursor: Any, statement: Any, parameters: Any, context: Any, is_disconnect: Any, invalidate_pool_on_disconnect: Any) -> None: ...

class Transaction(TransactionalContext):
    def __init__(self, connection: Any) -> None: ...
    @property
    def is_valid(self): ...
    def close(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...

class MarkerTransaction(Transaction):
    connection: Any = ...
    def __init__(self, connection: Any) -> None: ...
    @property
    def is_active(self): ...

class RootTransaction(Transaction):
    connection: Any = ...
    is_active: bool = ...
    def __init__(self, connection: Any) -> None: ...

class NestedTransaction(Transaction):
    connection: Any = ...
    is_active: bool = ...
    def __init__(self, connection: Any) -> None: ...

class TwoPhaseTransaction(RootTransaction):
    xid: Any = ...
    def __init__(self, connection: Any, xid: Any) -> None: ...
    def prepare(self) -> None: ...

class Engine(Connectable, log.Identified):
    pool: Any = ...
    url: Any = ...
    dialect: Any = ...
    logging_name: Any = ...
    echo: Any = ...
    hide_parameters: Any = ...
    def __init__(self, pool: Any, dialect: Any, url: Any, logging_name: Optional[Any] = ..., echo: Optional[Any] = ..., query_cache_size: int = ..., execution_options: Optional[Any] = ..., hide_parameters: bool = ...) -> None: ...
    @property
    def engine(self): ...
    def clear_compiled_cache(self) -> None: ...
    def update_execution_options(self, **opt: Any) -> None: ...
    def execution_options(self, **opt: Any): ...
    def get_execution_options(self): ...
    @property
    def name(self): ...
    @property
    def driver(self): ...
    def dispose(self) -> None: ...
    class _trans_ctx:
        conn: Any = ...
        transaction: Any = ...
        close_with_result: Any = ...
        def __init__(self, conn: Any, transaction: Any, close_with_result: Any) -> None: ...
        def __enter__(self): ...
        def __exit__(self, type_: Any, value: Any, traceback: Any) -> None: ...
    def begin(self, close_with_result: bool = ...): ...
    def transaction(self, callable_: Any, *args: Any, **kwargs: Any): ...
    def run_callable(self, callable_: Any, *args: Any, **kwargs: Any): ...
    def execute(self, statement: Any, *multiparams: Any, **params: Any): ...
    def scalar(self, statement: Any, *multiparams: Any, **params: Any): ...
    def connect(self, close_with_result: bool = ...): ...
    def table_names(self, schema: Optional[Any] = ..., connection: Optional[Any] = ...): ...
    def has_table(self, table_name: Any, schema: Optional[Any] = ...): ...
    def raw_connection(self, _connection: Optional[Any] = ...): ...

class OptionEngineMixin:
    url: Any = ...
    dialect: Any = ...
    logging_name: Any = ...
    echo: Any = ...
    hide_parameters: Any = ...
    dispatch: Any = ...
    def __init__(self, proxied: Any, execution_options: Any) -> None: ...
    pool: Any = ...

class OptionEngine(OptionEngineMixin, Engine): ...
