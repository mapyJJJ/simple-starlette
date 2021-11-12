from . import base as oracle
from ... import exc as exc, processors as processors, types as sqltypes, util as util
from ...util import compat as compat
from .base import OracleCompiler as OracleCompiler, OracleDialect as OracleDialect, OracleExecutionContext as OracleExecutionContext
from typing import Any, Optional

class _OracleInteger(sqltypes.Integer):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleNumeric(sqltypes.Numeric):
    is_number: bool = ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...

class _OracleBinaryFloat(_OracleNumeric):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleBINARY_FLOAT(_OracleBinaryFloat, oracle.BINARY_FLOAT): ...
class _OracleBINARY_DOUBLE(_OracleBinaryFloat, oracle.BINARY_DOUBLE): ...

class _OracleNUMBER(_OracleNumeric):
    is_number: bool = ...

class _OracleDate(sqltypes.Date):
    def bind_processor(self, dialect: Any) -> None: ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _OracleChar(sqltypes.CHAR):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleNChar(sqltypes.NCHAR):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleUnicodeStringNCHAR(oracle.NVARCHAR2):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleUnicodeStringCHAR(sqltypes.Unicode):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleUnicodeTextNCLOB(oracle.NCLOB):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleUnicodeTextCLOB(sqltypes.UnicodeText):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleText(sqltypes.Text):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleLong(oracle.LONG):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleString(sqltypes.String): ...

class _OracleEnum(sqltypes.Enum):
    def bind_processor(self, dialect: Any): ...

class _OracleBinary(sqltypes.LargeBinary):
    def get_dbapi_type(self, dbapi: Any): ...
    def bind_processor(self, dialect: Any) -> None: ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _OracleInterval(oracle.INTERVAL):
    def get_dbapi_type(self, dbapi: Any): ...

class _OracleRaw(oracle.RAW): ...

class _OracleRowid(oracle.ROWID):
    def get_dbapi_type(self, dbapi: Any): ...

class OracleCompiler_cx_oracle(OracleCompiler):
    def bindparam_string(self, name: Any, **kw: Any): ...

class OracleExecutionContext_cx_oracle(OracleExecutionContext):
    out_parameters: Any = ...
    include_set_input_sizes: Any = ...
    def pre_exec(self) -> None: ...
    cursor_fetch_strategy: Any = ...
    def post_exec(self) -> None: ...
    def create_cursor(self): ...
    def get_out_parameter_values(self, out_param_names: Any): ...

class OracleDialect_cx_oracle(OracleDialect):
    supports_statement_cache: bool = ...
    execution_ctx_cls: Any = ...
    statement_compiler: Any = ...
    supports_sane_rowcount: bool = ...
    supports_sane_multi_rowcount: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    use_setinputsizes: bool = ...
    driver: str = ...
    colspecs: Any = ...
    execute_sequence_format: Any = ...
    arraysize: Any = ...
    encoding_errors: Any = ...
    auto_convert_lobs: Any = ...
    coerce_to_unicode: Any = ...
    coerce_to_decimal: Any = ...
    cx_oracle_ver: Any = ...
    def __init__(self, auto_convert_lobs: bool = ..., coerce_to_unicode: bool = ..., coerce_to_decimal: bool = ..., arraysize: int = ..., encoding_errors: Optional[Any] = ..., threaded: Optional[Any] = ..., **kwargs: Any): ...
    @classmethod
    def dbapi(cls): ...
    def initialize(self, connection: Any) -> None: ...
    def get_isolation_level(self, connection: Any): ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
    def on_connect(self): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def create_xid(self): ...
    def do_executemany(self, cursor: Any, statement: Any, parameters: Any, context: Optional[Any] = ...) -> None: ...
    def do_begin_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_prepare_twophase(self, connection: Any, xid: Any) -> None: ...
    def do_rollback_twophase(self, connection: Any, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_commit_twophase(self, connection: Any, xid: Any, is_prepared: bool = ..., recover: bool = ...) -> None: ...
    def do_set_input_sizes(self, cursor: Any, list_of_tuples: Any, context: Any) -> None: ...
    def do_recover_twophase(self, connection: Any) -> None: ...
dialect = OracleDialect_cx_oracle
