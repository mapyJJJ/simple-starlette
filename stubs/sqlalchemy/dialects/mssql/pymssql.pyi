from ... import processors as processors, types as sqltypes, util as util
from .base import MSDialect as MSDialect, MSIdentifierPreparer as MSIdentifierPreparer
from typing import Any

class _MSNumeric_pymssql(sqltypes.Numeric):
    def result_processor(self, dialect: Any, type_: Any): ...

class MSIdentifierPreparer_pymssql(MSIdentifierPreparer):
    def __init__(self, dialect: Any) -> None: ...

class MSDialect_pymssql(MSDialect):
    supports_statement_cache: bool = ...
    supports_native_decimal: bool = ...
    driver: str = ...
    preparer: Any = ...
    colspecs: Any = ...
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
dialect = MSDialect_pymssql
