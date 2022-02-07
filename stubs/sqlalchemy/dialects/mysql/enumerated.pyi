from ... import exc as exc, sql as sql, util as util
from ...sql import sqltypes as sqltypes
from ...sql.base import NO_ARG as NO_ARG
from .types import _StringType
from typing import Any

class ENUM(sqltypes.NativeForEmulated, sqltypes.Enum, _StringType):
    __visit_name__: str = ...
    native_enum: bool = ...
    def __init__(self, *enums: Any, **kw: Any) -> None: ...
    @classmethod
    def adapt_emulated_to_native(cls, impl: Any, **kw: Any): ...

class SET(_StringType):
    __visit_name__: str = ...
    retrieve_as_bitwise: Any = ...
    values: Any = ...
    def __init__(self, *values: Any, **kw: Any) -> None: ...
    def column_expression(self, colexpr: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...
    def bind_processor(self, dialect: Any): ...
    def adapt(self, impltype: Any, **kw: Any): ...