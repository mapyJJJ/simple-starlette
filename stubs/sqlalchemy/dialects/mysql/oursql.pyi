from ... import util as util
from .base import BIT as BIT, MySQLDialect as MySQLDialect, MySQLExecutionContext as MySQLExecutionContext
from typing import Any, Optional

class _oursqlBIT(BIT):
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...

class MySQLExecutionContext_oursql(MySQLExecutionContext):
    @property
    def plain_query(self): ...

class MySQLDialect_oursql(MySQLDialect):
    driver: str = ...
    supports_statement_cache: bool = ...
    supports_unicode_binds: bool = ...
    supports_unicode_statements: bool = ...
    supports_native_decimal: bool = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    execution_ctx_cls: Any = ...
    colspecs: Any = ...
    @classmethod
    def dbapi(cls): ...
    def do_execute(self, cursor: Any, statement: Any, parameters: Any, context: Optional[Any] = ...) -> None: ...
    def do_begin(self, connection: Any) -> None: ...
    def do_begin_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_prepare_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_rollback_twophase(self, connection: Any, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection: Any, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def has_table(self, connection: Any, table_name: Any, schema: Optional[Any] = ...): ...
    def get_table_options(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_columns(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_view_names(self, connection: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_table_names(self, connection: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_schema_names(self, connection: Any, **kw: Any): ...
    def initialize(self, connection: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def create_connect_args(self, url: Any): ...
dialect = MySQLDialect_oursql
