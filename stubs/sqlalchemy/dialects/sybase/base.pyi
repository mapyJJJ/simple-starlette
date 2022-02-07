from sqlalchemy import exc as exc, types as sqltypes, util as util
from sqlalchemy.engine import default as default, reflection as reflection
from sqlalchemy.sql import compiler as compiler, text as text
from sqlalchemy.types import BIGINT as BIGINT, BINARY as BINARY, CHAR as CHAR, DATE as DATE, DATETIME as DATETIME, DECIMAL as DECIMAL, FLOAT as FLOAT, INT as INT, INTEGER as INTEGER, NCHAR as NCHAR, NUMERIC as NUMERIC, NVARCHAR as NVARCHAR, REAL as REAL, SMALLINT as SMALLINT, TEXT as TEXT, TIME as TIME, TIMESTAMP as TIMESTAMP, Unicode as Unicode, VARBINARY as VARBINARY, VARCHAR as VARCHAR
from typing import Any, Optional

RESERVED_WORDS: Any

class _SybaseUnitypeMixin:
    def result_processor(self, dialect: Any, coltype: Any): ...

class UNICHAR(_SybaseUnitypeMixin, sqltypes.Unicode):
    __visit_name__: str = ...

class UNIVARCHAR(_SybaseUnitypeMixin, sqltypes.Unicode):
    __visit_name__: str = ...

class UNITEXT(_SybaseUnitypeMixin, sqltypes.UnicodeText):
    __visit_name__: str = ...

class TINYINT(sqltypes.Integer):
    __visit_name__: str = ...

class BIT(sqltypes.TypeEngine):
    __visit_name__: str = ...

class MONEY(sqltypes.TypeEngine):
    __visit_name__: str = ...

class SMALLMONEY(sqltypes.TypeEngine):
    __visit_name__: str = ...

class UNIQUEIDENTIFIER(sqltypes.TypeEngine):
    __visit_name__: str = ...

class IMAGE(sqltypes.LargeBinary):
    __visit_name__: str = ...

class SybaseTypeCompiler(compiler.GenericTypeCompiler):
    def visit_large_binary(self, type_: Any, **kw: Any): ...
    def visit_boolean(self, type_: Any, **kw: Any): ...
    def visit_unicode(self, type_: Any, **kw: Any): ...
    def visit_UNICHAR(self, type_: Any, **kw: Any): ...
    def visit_UNIVARCHAR(self, type_: Any, **kw: Any): ...
    def visit_UNITEXT(self, type_: Any, **kw: Any): ...
    def visit_TINYINT(self, type_: Any, **kw: Any): ...
    def visit_IMAGE(self, type_: Any, **kw: Any): ...
    def visit_BIT(self, type_: Any, **kw: Any): ...
    def visit_MONEY(self, type_: Any, **kw: Any): ...
    def visit_SMALLMONEY(self, type_: Any, **kw: Any): ...
    def visit_UNIQUEIDENTIFIER(self, type_: Any, **kw: Any): ...

ischema_names: Any

class SybaseInspector(reflection.Inspector):
    def __init__(self, conn: Any) -> None: ...
    def get_table_id(self, table_name: Any, schema: Optional[Any] = ...): ...

class SybaseExecutionContext(default.DefaultExecutionContext):
    def set_ddl_autocommit(self, connection: Any, value: Any) -> None: ...
    def pre_exec(self) -> None: ...
    def post_exec(self) -> None: ...
    def get_lastrowid(self): ...

class SybaseSQLCompiler(compiler.SQLCompiler):
    ansi_bind_rules: bool = ...
    extract_map: Any = ...
    def get_from_hint_text(self, table: Any, text: Any): ...
    def limit_clause(self, select: Any, **kw: Any): ...
    def visit_extract(self, extract: Any, **kw: Any): ...
    def visit_now_func(self, fn: Any, **kw: Any): ...
    def for_update_clause(self, select: Any): ...
    def order_by_clause(self, select: Any, **kw: Any): ...
    def delete_table_clause(self, delete_stmt: Any, from_table: Any, extra_froms: Any): ...
    def delete_extra_from_clause(self, delete_stmt: Any, from_table: Any, extra_froms: Any, from_hints: Any, **kw: Any): ...

class SybaseDDLCompiler(compiler.DDLCompiler):
    def get_column_specification(self, column: Any, **kwargs: Any): ...
    def visit_drop_index(self, drop: Any): ...

class SybaseIdentifierPreparer(compiler.IdentifierPreparer):
    reserved_words: Any = ...

class SybaseDialect(default.DefaultDialect):
    name: str = ...
    supports_unicode_statements: bool = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    supports_statement_cache: bool = ...
    supports_native_boolean: bool = ...
    supports_unicode_binds: bool = ...
    postfetch_lastrowid: bool = ...
    colspecs: Any = ...
    ischema_names: Any = ...
    type_compiler: Any = ...
    statement_compiler: Any = ...
    ddl_compiler: Any = ...
    preparer: Any = ...
    inspector: Any = ...
    construct_arguments: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    max_identifier_length: int = ...
    def initialize(self, connection: Any) -> None: ...
    def get_table_id(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_columns(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_foreign_keys(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_indexes(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_pk_constraint(self, connection: Any, table_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_schema_names(self, connection: Any, **kw: Any): ...
    def get_table_names(self, connection: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_view_definition(self, connection: Any, view_name: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def get_view_names(self, connection: Any, schema: Optional[Any] = ..., **kw: Any): ...
    def has_table(self, connection: Any, table_name: Any, schema: Optional[Any] = ...): ...
