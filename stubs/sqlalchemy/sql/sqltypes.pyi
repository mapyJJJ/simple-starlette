from . import coercions as coercions, elements as elements, operators as operators, roles as roles, type_api as type_api
from .. import event as event, exc as exc, inspection as inspection, processors as processors, util as util
from ..util import OrderedDict as OrderedDict, compat as compat, langhelpers as langhelpers, pickle as pickle
from .base import NO_ARG as NO_ARG, SchemaEventTarget as SchemaEventTarget
from .elements import Slice as Slice, quoted_name as quoted_name
from .traversals import HasCacheKey as HasCacheKey, InternalTraversal as InternalTraversal
from .type_api import Emulated as Emulated, NativeForEmulated as NativeForEmulated, TypeDecorator as TypeDecorator, TypeEngine as TypeEngine, Variant as Variant, to_instance as to_instance
from typing import Any, Optional

class _LookupExpressionAdapter:
    class Comparator(TypeEngine.Comparator): ...
    comparator_factory: Any = ...

class Concatenable:
    class Comparator(TypeEngine.Comparator): ...
    comparator_factory: Any = ...

class Indexable:
    class Comparator(TypeEngine.Comparator):
        def __getitem__(self, index: Any): ...
    comparator_factory: Any = ...

class String(Concatenable, TypeEngine):
    __visit_name__: str = ...
    RETURNS_UNICODE: Any = ...
    RETURNS_BYTES: Any = ...
    RETURNS_CONDITIONAL: Any = ...
    RETURNS_UNKNOWN: Any = ...
    length: Any = ...
    collation: Any = ...
    def __init__(self, length: Optional[Any] = ..., collation: Optional[Any] = ..., convert_unicode: bool = ..., unicode_error: Optional[Any] = ..., _warn_on_bytestring: bool = ..., _expect_unicode: bool = ...) -> None: ...
    def literal_processor(self, dialect: Any): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...
    @property
    def python_type(self): ...
    def get_dbapi_type(self, dbapi: Any): ...

class Text(String):
    __visit_name__: str = ...

class Unicode(String):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None: ...

class UnicodeText(Text):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None: ...

class Integer(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str = ...
    def get_dbapi_type(self, dbapi: Any): ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect: Any): ...

class SmallInteger(Integer):
    __visit_name__: str = ...

class BigInteger(Integer):
    __visit_name__: str = ...

class Numeric(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str = ...
    precision: Any = ...
    scale: Any = ...
    decimal_return_scale: Any = ...
    asdecimal: Any = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., decimal_return_scale: Optional[Any] = ..., asdecimal: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any): ...
    def literal_processor(self, dialect: Any): ...
    @property
    def python_type(self): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class Float(Numeric):
    __visit_name__: str = ...
    scale: Any = ...
    precision: Any = ...
    asdecimal: Any = ...
    decimal_return_scale: Any = ...
    def __init__(self, precision: Optional[Any] = ..., asdecimal: bool = ..., decimal_return_scale: Optional[Any] = ...) -> None: ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class DateTime(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str = ...
    timezone: Any = ...
    def __init__(self, timezone: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any): ...
    @property
    def python_type(self): ...

class Date(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str = ...
    def get_dbapi_type(self, dbapi: Any): ...
    @property
    def python_type(self): ...

class Time(_LookupExpressionAdapter, TypeEngine):
    __visit_name__: str = ...
    timezone: Any = ...
    def __init__(self, timezone: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any): ...
    @property
    def python_type(self): ...

class _Binary(TypeEngine):
    length: Any = ...
    def __init__(self, length: Optional[Any] = ...) -> None: ...
    def literal_processor(self, dialect: Any): ...
    @property
    def python_type(self): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...
    def coerce_compared_value(self, op: Any, value: Any): ...
    def get_dbapi_type(self, dbapi: Any): ...

class LargeBinary(_Binary):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ...) -> None: ...

class SchemaType(SchemaEventTarget):
    name: Any = ...
    schema: Any = ...
    metadata: Any = ...
    inherit_schema: Any = ...
    def __init__(self, name: Optional[Any] = ..., schema: Optional[Any] = ..., metadata: Optional[Any] = ..., inherit_schema: bool = ..., quote: Optional[Any] = ..., _create_events: bool = ...) -> None: ...
    def copy(self, **kw: Any): ...
    def adapt(self, impltype: Any, **kw: Any): ...
    @property
    def bind(self): ...
    def create(self, bind: Optional[Any] = ..., checkfirst: bool = ...) -> None: ...
    def drop(self, bind: Optional[Any] = ..., checkfirst: bool = ...) -> None: ...

class Enum(Emulated, String, SchemaType):
    __visit_name__: str = ...
    def __init__(self, *enums: Any, **kw: Any) -> None: ...
    @property
    def sort_key_function(self): ...
    @property
    def native(self): ...
    class Comparator(String.Comparator): ...
    comparator_factory: Any = ...
    def as_generic(self, allow_nulltype: bool = ...): ...
    def adapt_to_emulated(self, impltype: Any, **kw: Any): ...
    def adapt(self, impltype: Any, **kw: Any): ...
    def literal_processor(self, dialect: Any): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...
    def copy(self, **kw: Any): ...
    @property
    def python_type(self): ...

class PickleType(TypeDecorator):
    impl: Any = ...
    cache_ok: bool = ...
    protocol: Any = ...
    pickler: Any = ...
    comparator: Any = ...
    def __init__(self, protocol: Any = ..., pickler: Optional[Any] = ..., comparator: Optional[Any] = ..., impl: Optional[Any] = ...) -> None: ...
    def __reduce__(self): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...
    def compare_values(self, x: Any, y: Any): ...

class Boolean(Emulated, TypeEngine, SchemaType):
    __visit_name__: str = ...
    native: bool = ...
    create_constraint: Any = ...
    name: Any = ...
    def __init__(self, create_constraint: bool = ..., name: Optional[Any] = ..., _create_events: bool = ...) -> None: ...
    @property
    def python_type(self): ...
    def literal_processor(self, dialect: Any): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class _AbstractInterval(_LookupExpressionAdapter, TypeEngine):
    def coerce_compared_value(self, op: Any, value: Any): ...

class Interval(Emulated, _AbstractInterval, TypeDecorator):
    impl: Any = ...
    epoch: Any = ...
    cache_ok: bool = ...
    native: Any = ...
    second_precision: Any = ...
    day_precision: Any = ...
    def __init__(self, native: bool = ..., second_precision: Optional[Any] = ..., day_precision: Optional[Any] = ...) -> None: ...
    @property
    def python_type(self): ...
    def adapt_to_emulated(self, impltype: Any, **kw: Any): ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class JSON(Indexable, TypeEngine):
    __visit_name__: str = ...
    hashable: bool = ...
    NULL: Any = ...
    none_as_null: Any = ...
    def __init__(self, none_as_null: bool = ...) -> None: ...
    class JSONElementType(TypeEngine):
        def string_bind_processor(self, dialect: Any): ...
        def string_literal_processor(self, dialect: Any): ...
        def bind_processor(self, dialect: Any): ...
        def literal_processor(self, dialect: Any): ...
    class JSONIndexType(JSONElementType): ...
    class JSONIntIndexType(JSONIndexType): ...
    class JSONStrIndexType(JSONIndexType): ...
    class JSONPathType(JSONElementType): ...
    class Comparator(Indexable.Comparator, Concatenable.Comparator):
        def as_boolean(self): ...
        def as_string(self): ...
        def as_integer(self): ...
        def as_float(self): ...
        def as_numeric(self, precision: Any, scale: Any, asdecimal: bool = ...): ...
        def as_json(self): ...
    comparator_factory: Any = ...
    @property
    def python_type(self): ...
    @property
    def should_evaluate_none(self): ...
    @should_evaluate_none.setter
    def should_evaluate_none(self, value: Any) -> None: ...
    def bind_processor(self, dialect: Any): ...
    def result_processor(self, dialect: Any, coltype: Any): ...

class ARRAY(SchemaEventTarget, Indexable, Concatenable, TypeEngine):
    __visit_name__: str = ...
    zero_indexes: bool = ...
    class Comparator(Indexable.Comparator, Concatenable.Comparator):
        def contains(self, *arg: Any, **kw: Any) -> None: ...
        def any(self, other: Any, operator: Optional[Any] = ...): ...
        def all(self, other: Any, operator: Optional[Any] = ...): ...
    comparator_factory: Any = ...
    item_type: Any = ...
    as_tuple: Any = ...
    dimensions: Any = ...
    def __init__(self, item_type: Any, as_tuple: bool = ..., dimensions: Optional[Any] = ..., zero_indexes: bool = ...) -> None: ...
    @property
    def hashable(self): ...
    @property
    def python_type(self): ...
    def compare_values(self, x: Any, y: Any): ...

class TupleType(TypeEngine):
    types: Any = ...
    def __init__(self, *types: Any) -> None: ...
    def result_processor(self, dialect: Any, coltype: Any) -> None: ...

class REAL(Float):
    __visit_name__: str = ...

class FLOAT(Float):
    __visit_name__: str = ...

class NUMERIC(Numeric):
    __visit_name__: str = ...

class DECIMAL(Numeric):
    __visit_name__: str = ...

class INTEGER(Integer):
    __visit_name__: str = ...
INT = INTEGER

class SMALLINT(SmallInteger):
    __visit_name__: str = ...

class BIGINT(BigInteger):
    __visit_name__: str = ...

class TIMESTAMP(DateTime):
    __visit_name__: str = ...
    def __init__(self, timezone: bool = ...) -> None: ...
    def get_dbapi_type(self, dbapi: Any): ...

class DATETIME(DateTime):
    __visit_name__: str = ...

class DATE(Date):
    __visit_name__: str = ...

class TIME(Time):
    __visit_name__: str = ...

class TEXT(Text):
    __visit_name__: str = ...

class CLOB(Text):
    __visit_name__: str = ...

class VARCHAR(String):
    __visit_name__: str = ...

class NVARCHAR(Unicode):
    __visit_name__: str = ...

class CHAR(String):
    __visit_name__: str = ...

class NCHAR(Unicode):
    __visit_name__: str = ...

class BLOB(LargeBinary):
    __visit_name__: str = ...

class BINARY(_Binary):
    __visit_name__: str = ...

class VARBINARY(_Binary):
    __visit_name__: str = ...

class BOOLEAN(Boolean):
    __visit_name__: str = ...

class NullType(TypeEngine):
    __visit_name__: str = ...
    def literal_processor(self, dialect: Any): ...
    class Comparator(TypeEngine.Comparator): ...
    comparator_factory: Any = ...

class TableValueType(HasCacheKey, TypeEngine):
    def __init__(self, *elements: Any) -> None: ...

class MatchType(Boolean): ...

NULLTYPE: Any
BOOLEANTYPE: Any
STRINGTYPE: Any
INTEGERTYPE: Any
MATCHTYPE: Any
TABLEVALUE: Any
