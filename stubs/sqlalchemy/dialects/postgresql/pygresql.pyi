from ... import exc as exc, processors as processors, util as util
from ...sql.elements import Null as Null
from ...types import Numeric as Numeric
from .base import PGCompiler as PGCompiler, PGDialect as PGDialect, PGIdentifierPreparer as PGIdentifierPreparer, UUID as UUID
from .hstore import HSTORE as HSTORE
from .json import JSON as JSON, JSONB as JSONB
from typing import Any

class _PGNumeric(Numeric):
    def bind_processor(self, dialect: Any) -> None: ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGHStore(HSTORE):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGJSON(JSON):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGJSONB(JSONB):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGUUID(UUID):
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _PGCompiler(PGCompiler):
    def visit_mod_binary(self, binary: Any, operator: Any, **kw: Any): ...
    def post_process_text(self, text: Any): ...

class _PGIdentifierPreparer(PGIdentifierPreparer): ...

class PGDialect_pygresql(PGDialect):
    driver: str = ...
    supports_statement_cache: bool = ...
    statement_compiler: Any = ...
    preparer: Any = ...
    @classmethod
    def dbapi(cls): ...
    colspecs: Any = ...
    dbapi_version: Any = ...
    supports_unicode_statements: bool = ...
    supports_unicode_binds: bool = ...
    has_native_hstore: Any = ...
    has_native_json: Any = ...
    has_native_uuid: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def create_connect_args(self, url: Any): ...
    def is_disconnect(self, e: Any, connection: Any, cursor: Any): ...
dialect = PGDialect_pygresql
