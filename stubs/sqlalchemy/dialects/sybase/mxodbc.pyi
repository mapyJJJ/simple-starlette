from sqlalchemy.connectors.mxodbc import MxODBCConnector as MxODBCConnector
from sqlalchemy.dialects.sybase.base import SybaseDialect as SybaseDialect, SybaseExecutionContext as SybaseExecutionContext
from typing import Any

class SybaseExecutionContext_mxodbc(SybaseExecutionContext): ...

class SybaseDialect_mxodbc(MxODBCConnector, SybaseDialect):
    execution_ctx_cls: Any = ...
    supports_statement_cache: bool = ...
dialect = SybaseDialect_mxodbc
