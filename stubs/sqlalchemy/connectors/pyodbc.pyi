from . import Connector as Connector
from .. import util as util
from typing import Any, Optional

class PyODBCConnector(Connector):
    driver: str = ...
    supports_sane_rowcount_returning: bool = ...
    supports_sane_multi_rowcount: bool = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    supports_native_decimal: bool = ...
    default_paramstyle: str = ...
    use_setinputsizes: bool = ...
    pyodbc_driver_name: Any = ...
    def __init__(self, supports_unicode_binds: Optional[Any] = ..., use_setinputsizes: bool = ..., **kw: Any) -> None: ...
    @classmethod
    def dbapi(cls): ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
    def do_set_input_sizes(self, cursor: Any, list_of_tuples: Any, context: Any) -> None: ...
    def set_isolation_level(self, connection: Any, level: Any) -> None: ...
