from .base import MariaDBIdentifierPreparer as MariaDBIdentifierPreparer, MySQLDialect as MySQLDialect
from typing import Any

class MariaDBDialect(MySQLDialect):
    is_mariadb: bool = ...
    supports_statement_cache: bool = ...
    name: str = ...
    preparer: Any = ...

def loader(driver: Any): ...