from .psycopg2 import PGDialect_psycopg2 as PGDialect_psycopg2
from typing import Any

class PGDialect_psycopg2cffi(PGDialect_psycopg2):
    driver: str = ...
    supports_unicode_statements: bool = ...
    supports_statement_cache: bool = ...
    FEATURE_VERSION_MAP: Any = ...
    @classmethod
    def dbapi(cls): ...
dialect = PGDialect_psycopg2cffi
