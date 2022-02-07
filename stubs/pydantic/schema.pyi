from typing import Any, Callable, ClassVar, Dict, Iterable, List, Optional, Tuple, Union

import datetime
import decimal
import ipaddress
import pathlib
import pydantic.utils
import typing
Any: typing._SpecialForm
Callable: typing._VariadicGenericAlias
Dict: typing._GenericAlias
FrozenSet: typing._GenericAlias
Iterable: typing._GenericAlias
List: typing._GenericAlias
Literal: typing._SpecialForm
MAPPING_LIKE_SHAPES: set
NONE_TYPES: set
Optional: typing._SpecialForm
Pattern: typing._GenericAlias
ROOT_KEY: str
SHAPE_FROZENSET: int
SHAPE_GENERIC: int
SHAPE_ITERABLE: int
SHAPE_LIST: int
SHAPE_SEQUENCE: int
SHAPE_SET: int
SHAPE_SINGLETON: int
SHAPE_TUPLE: int
SHAPE_TUPLE_ELLIPSIS: int
Sequence: typing._GenericAlias
Set: typing._GenericAlias
TYPE_CHECKING: bool
Tuple: typing._VariadicGenericAlias
Type: typing._GenericAlias
TypeModelOrEnum: typing._GenericAlias
TypeModelSet: typing._GenericAlias
Union: typing._SpecialForm
_map_types_constraint: dict
_numeric_types_attrs: tuple
_str_types_attrs: tuple
add_field_type_to_schema: cython_function_or_method
all_literal_values: cython_function_or_method
cast: function
conbytes: cython_function_or_method
condecimal: cython_function_or_method
confloat: cython_function_or_method
conint: cython_function_or_method
conlist: cython_function_or_method
conset: cython_function_or_method
constr: cython_function_or_method
default_prefix: str
default_ref_template: str
encode_default: cython_function_or_method
enum_process_schema: cython_function_or_method
field_class_to_schema: tuple
field_schema: cython_function_or_method
field_singleton_schema: cython_function_or_method
field_singleton_sub_fields_schema: cython_function_or_method
field_type_schema: cython_function_or_method
get_annotation_from_field_info: cython_function_or_method
get_annotation_with_constraints: cython_function_or_method
get_args: cython_function_or_method
get_field_info_schema: cython_function_or_method
get_field_schema_validations: cython_function_or_method
get_flat_models_from_field: cython_function_or_method
get_flat_models_from_fields: cython_function_or_method
get_flat_models_from_model: cython_function_or_method
get_flat_models_from_models: cython_function_or_method
get_long_model_name: cython_function_or_method
get_model: cython_function_or_method
get_model_name_map: cython_function_or_method
get_origin: cython_function_or_method
get_schema_ref: cython_function_or_method
is_callable_type: cython_function_or_method
is_literal_type: cython_function_or_method
is_namedtuple: cython_function_or_method
json_scheme: dict
lenient_issubclass: cython_function_or_method
model_process_schema: cython_function_or_method
model_schema: cython_function_or_method
model_type_schema: cython_function_or_method
multitypes_literal_field_for_schema: cython_function_or_method
normalize_name: cython_function_or_method
numeric_types: tuple
pydantic_encoder: cython_function_or_method
schema: cython_function_or_method
sequence_like: cython_function_or_method

class Annotated:
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __class_getitem__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __init_subclass__(self, *args, **kwargs) -> Any: ...

class AnyUrl(str):
    allowed_schemes: ClassVar[None] = ...
    fragment: ClassVar[member_descriptor] = ...
    host: ClassVar[member_descriptor] = ...
    host_type: ClassVar[member_descriptor] = ...
    max_length: ClassVar[int] = ...
    min_length: ClassVar[int] = ...
    password: ClassVar[member_descriptor] = ...
    path: ClassVar[member_descriptor] = ...
    port: ClassVar[member_descriptor] = ...
    query: ClassVar[member_descriptor] = ...
    scheme: ClassVar[member_descriptor] = ...
    strip_whitespace: ClassVar[bool] = ...
    tld: ClassVar[member_descriptor] = ...
    tld_required: ClassVar[bool] = ...
    user: ClassVar[member_descriptor] = ...
    user_required: ClassVar[bool] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def build(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate_host(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate_parts(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class ConstrainedDecimal(decimal.Decimal):
    decimal_places: ClassVar[None] = ...
    ge: ClassVar[None] = ...
    gt: ClassVar[None] = ...
    le: ClassVar[None] = ...
    lt: ClassVar[None] = ...
    max_digits: ClassVar[None] = ...
    multiple_of: ClassVar[None] = ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class ConstrainedFloat(float):
    ge: ClassVar[None] = ...
    gt: ClassVar[None] = ...
    le: ClassVar[None] = ...
    lt: ClassVar[None] = ...
    multiple_of: ClassVar[None] = ...
    strict: ClassVar[bool] = ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class ConstrainedInt(int):
    ge: ClassVar[None] = ...
    gt: ClassVar[None] = ...
    le: ClassVar[None] = ...
    lt: ClassVar[None] = ...
    multiple_of: ClassVar[None] = ...
    strict: ClassVar[bool] = ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class ConstrainedList(list):
    class __origin__:
        __hash__: ClassVar[None] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def append(self, *args, **kwargs) -> Any: ...
        def clear(self, *args, **kwargs) -> Any: ...
        def copy(self, *args, **kwargs) -> Any: ...
        def count(self, *args, **kwargs) -> Any: ...
        def extend(self, *args, **kwargs) -> Any: ...
        def index(self, *args, **kwargs) -> Any: ...
        def insert(self, *args, **kwargs) -> Any: ...
        def pop(self, *args, **kwargs) -> Any: ...
        def remove(self, *args, **kwargs) -> Any: ...
        def reverse(self, *args, **kwargs) -> Any: ...
        def sort(self, *args, **kwargs) -> Any: ...
        def __add__(self, other) -> Any: ...
        def __contains__(self, other) -> Any: ...
        def __delitem__(self, other) -> Any: ...
        def __eq__(self, other) -> Any: ...
        def __ge__(self, other) -> Any: ...
        def __getitem__(y) -> Any: ...
        def __gt__(self, other) -> Any: ...
        def __iadd__(self, other) -> Any: ...
        def __imul__(self, other) -> Any: ...
        def __iter__(self) -> Any: ...
        def __le__(self, other) -> Any: ...
        def __len__(self) -> Any: ...
        def __lt__(self, other) -> Any: ...
        def __mul__(self, other) -> Any: ...
        def __ne__(self, other) -> Any: ...
        def __reversed__(self) -> Any: ...
        def __rmul__(self, other) -> Any: ...
        def __setitem__(self, index, object) -> Any: ...
        def __sizeof__(self) -> Any: ...
    max_items: ClassVar[None] = ...
    min_items: ClassVar[None] = ...
    @classmethod
    def list_length_validator(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class ConstrainedSet(set):
    class __origin__:
        __hash__: ClassVar[None] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def add(self, *args, **kwargs) -> Any: ...
        def clear(self, *args, **kwargs) -> Any: ...
        def copy(self, *args, **kwargs) -> Any: ...
        def difference(self, *args, **kwargs) -> Any: ...
        def difference_update(self, *args, **kwargs) -> Any: ...
        def discard(self, *args, **kwargs) -> Any: ...
        def intersection(self, *args, **kwargs) -> Any: ...
        def intersection_update(self, *args, **kwargs) -> Any: ...
        def isdisjoint(self, *args, **kwargs) -> Any: ...
        def issubset(self, *args, **kwargs) -> Any: ...
        def issuperset(self, *args, **kwargs) -> Any: ...
        def pop(self, *args, **kwargs) -> Any: ...
        def remove(self, *args, **kwargs) -> Any: ...
        def symmetric_difference(self, *args, **kwargs) -> Any: ...
        def symmetric_difference_update(self, *args, **kwargs) -> Any: ...
        def union(self, *args, **kwargs) -> Any: ...
        def update(self, *args, **kwargs) -> Any: ...
        def __and__(self, other) -> Any: ...
        def __contains__(y) -> Any: ...
        def __eq__(self, other) -> Any: ...
        def __ge__(self, other) -> Any: ...
        def __gt__(self, other) -> Any: ...
        def __iand__(self, other) -> Any: ...
        def __ior__(self, other) -> Any: ...
        def __isub__(self, other) -> Any: ...
        def __iter__(self) -> Any: ...
        def __ixor__(self, other) -> Any: ...
        def __le__(self, other) -> Any: ...
        def __len__(self) -> Any: ...
        def __lt__(self, other) -> Any: ...
        def __ne__(self, other) -> Any: ...
        def __or__(self, other) -> Any: ...
        def __rand__(self, other) -> Any: ...
        def __reduce__(self) -> Any: ...
        def __ror__(self, other) -> Any: ...
        def __rsub__(self, other) -> Any: ...
        def __rxor__(self, other) -> Any: ...
        def __sizeof__(self) -> Any: ...
        def __sub__(self, other) -> Any: ...
        def __xor__(self, other) -> Any: ...
    max_items: ClassVar[None] = ...
    min_items: ClassVar[None] = ...
    @classmethod
    def set_length_validator(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class ConstrainedStr(str):
    curtail_length: ClassVar[None] = ...
    max_length: ClassVar[None] = ...
    min_length: ClassVar[None] = ...
    regex: ClassVar[None] = ...
    strict: ClassVar[bool] = ...
    strip_whitespace: ClassVar[bool] = ...
    to_lower: ClassVar[bool] = ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class Decimal:
    imag: ClassVar[getset_descriptor] = ...
    real: ClassVar[getset_descriptor] = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def adjusted(self, *args, **kwargs) -> Any: ...
    def as_integer_ratio(self, *args, **kwargs) -> Any: ...
    def as_tuple(self, *args, **kwargs) -> Any: ...
    def canonical(self, *args, **kwargs) -> Any: ...
    def compare(self, *args, **kwargs) -> Any: ...
    def compare_signal(self, *args, **kwargs) -> Any: ...
    def compare_total(self, *args, **kwargs) -> Any: ...
    def compare_total_mag(y) -> Any: ...
    def conjugate(self, *args, **kwargs) -> Any: ...
    def copy_abs(self, *args, **kwargs) -> Any: ...
    def copy_negate(self, *args, **kwargs) -> Any: ...
    def copy_sign(self, *args, **kwargs) -> Any: ...
    def exp(self, *args, **kwargs) -> Any: ...
    def fma(self, *args, **kwargs) -> Any: ...
    @classmethod
    def from_float(self, *args, **kwargs) -> Any: ...
    def is_canonical(self, *args, **kwargs) -> Any: ...
    def is_finite(self, *args, **kwargs) -> Any: ...
    def is_infinite(self, *args, **kwargs) -> Any: ...
    def is_nan(self, *args, **kwargs) -> Any: ...
    def is_normal(self, *args, **kwargs) -> Any: ...
    def is_qnan(self, *args, **kwargs) -> Any: ...
    def is_signed(self, *args, **kwargs) -> Any: ...
    def is_snan(self, *args, **kwargs) -> Any: ...
    def is_subnormal(self, *args, **kwargs) -> Any: ...
    def is_zero(self, *args, **kwargs) -> Any: ...
    def ln(self, *args, **kwargs) -> Any: ...
    def log10(self, *args, **kwargs) -> Any: ...
    def logb(self, *args, **kwargs) -> Any: ...
    def logical_and(self, *args, **kwargs) -> Any: ...
    def logical_invert(self, *args, **kwargs) -> Any: ...
    def logical_or(self, *args, **kwargs) -> Any: ...
    def logical_xor(self, *args, **kwargs) -> Any: ...
    def max(self, *args, **kwargs) -> Any: ...
    def max_mag(self, *args, **kwargs) -> Any: ...
    def min(self, *args, **kwargs) -> Any: ...
    def min_mag(self, *args, **kwargs) -> Any: ...
    def next_minus(self, *args, **kwargs) -> Any: ...
    def next_plus(self, *args, **kwargs) -> Any: ...
    def next_toward(self, *args, **kwargs) -> Any: ...
    def normalize(self, *args, **kwargs) -> Any: ...
    def number_class(self, *args, **kwargs) -> Any: ...
    def quantize(self, *args, **kwargs) -> Any: ...
    def radix(base) -> Any: ...
    def remainder_near(self, *args, **kwargs) -> Any: ...
    def rotate(self, *args, **kwargs) -> Any: ...
    def same_quantum(self, *args, **kwargs) -> Any: ...
    def scaleb(self, *args, **kwargs) -> Any: ...
    def shift(self, *args, **kwargs) -> Any: ...
    def sqrt(self, *args, **kwargs) -> Any: ...
    def to_eng_string(self, *args, **kwargs) -> Any: ...
    def to_integral() -> Any: ...
    def to_integral_exact(self, *args, **kwargs) -> Any: ...
    def to_integral_value(self, *args, **kwargs) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    def __ceil__(self, *args, **kwargs) -> Any: ...
    def __complex__(self) -> Any: ...
    def __copy__(self) -> Any: ...
    def __deepcopy__(self) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __float__(self) -> Any: ...
    def __floor__(self, *args, **kwargs) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __format__(self, *args, **kwargs) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __int__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __pos__(self) -> Any: ...
    def __pow__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __round__(self) -> Any: ...
    def __rpow__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __sizeof__(self) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...
    def __trunc__(self) -> Any: ...

class EmailStr(str):
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class Enum:
    class _member_type_:
        __class__: ClassVar[getset_descriptor] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def __delattr__(self, name) -> Any: ...
        def __dir__(self) -> Any: ...
        def __eq__(self, other) -> Any: ...
        def __format__(self, *args, **kwargs) -> Any: ...
        def __ge__(self, other) -> Any: ...
        def __gt__(self, other) -> Any: ...
        def __hash__(self) -> Any: ...
        @classmethod
        def __init_subclass__(self, *args, **kwargs) -> Any: ...
        def __le__(self, other) -> Any: ...
        def __lt__(self, other) -> Any: ...
        def __ne__(self, other) -> Any: ...
        def __reduce__(self) -> Any: ...
        def __reduce_ex__(self, protocol) -> Any: ...
        def __setattr__(self, name, value) -> Any: ...
        def __sizeof__(self) -> Any: ...
        @classmethod
        def __subclasshook__(self, *args, **kwargs) -> Any: ...
    _generate_next_value_: ClassVar[function] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _value2member_map_: ClassVar[dict] = ...
    __dir__: ClassVar[function] = ...
    __format__: ClassVar[function] = ...
    __hash__: ClassVar[function] = ...
    __reduce_ex__: ClassVar[function] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def _missing_(self, *args, **kwargs) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def value(self) -> Any: ...

class FieldInfo(pydantic.utils.Representation):
    alias: ClassVar[member_descriptor] = ...
    alias_priority: ClassVar[member_descriptor] = ...
    allow_mutation: ClassVar[member_descriptor] = ...
    const: ClassVar[member_descriptor] = ...
    default: ClassVar[member_descriptor] = ...
    default_factory: ClassVar[member_descriptor] = ...
    description: ClassVar[member_descriptor] = ...
    extra: ClassVar[member_descriptor] = ...
    ge: ClassVar[member_descriptor] = ...
    gt: ClassVar[member_descriptor] = ...
    le: ClassVar[member_descriptor] = ...
    lt: ClassVar[member_descriptor] = ...
    max_items: ClassVar[member_descriptor] = ...
    max_length: ClassVar[member_descriptor] = ...
    min_items: ClassVar[member_descriptor] = ...
    min_length: ClassVar[member_descriptor] = ...
    multiple_of: ClassVar[member_descriptor] = ...
    regex: ClassVar[member_descriptor] = ...
    title: ClassVar[member_descriptor] = ...
    __field_constraints__: ClassVar[dict] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _validate(self, *args, **kwargs) -> Any: ...
    def get_constraints(self, *args, **kwargs) -> Any: ...
    def update_from_config(self, *args, **kwargs) -> Any: ...
    def __repr_args__(self, *args, **kwargs) -> Any: ...

class ForwardRef(typing._Final):
    __init__: ClassVar[function] = ...
    _evaluate: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __forward_arg__: ClassVar[member_descriptor] = ...
    __forward_code__: ClassVar[member_descriptor] = ...
    __forward_evaluated__: ClassVar[member_descriptor] = ...
    __forward_is_argument__: ClassVar[member_descriptor] = ...
    __forward_value__: ClassVar[member_descriptor] = ...
    __hash__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...

class Generic:
    _is_protocol: ClassVar[bool] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __class_getitem__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __init_subclass__(self, *args, **kwargs) -> Any: ...

class IPv4Address(ipaddress._BaseV4, ipaddress._BaseAddress):
    class _constants:
        _linklocal_network: ClassVar[ipaddress.IPv4Network] = ...
        _loopback_network: ClassVar[ipaddress.IPv4Network] = ...
        _multicast_network: ClassVar[ipaddress.IPv4Network] = ...
        _private_networks: ClassVar[list] = ...
        _public_network: ClassVar[ipaddress.IPv4Network] = ...
        _reserved_network: ClassVar[ipaddress.IPv4Network] = ...
        _unspecified_address: ClassVar[ipaddress.IPv4Address] = ...
    __init__: ClassVar[function] = ...
    _ip: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    @property
    def is_global(self) -> Any: ...
    @property
    def is_link_local(self) -> Any: ...
    @property
    def is_loopback(self) -> Any: ...
    @property
    def is_multicast(self) -> Any: ...
    @property
    def is_private(self) -> Any: ...
    @property
    def is_reserved(self) -> Any: ...
    @property
    def is_unspecified(self) -> Any: ...
    @property
    def packed(self) -> Any: ...

class IPv4Interface(ipaddress.IPv4Address):
    __init__: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __hash__: ClassVar[function] = ...
    __lt__: ClassVar[function] = ...
    __reduce__: ClassVar[function] = ...
    def hostmask(self, *args, **kwargs) -> Any: ...
    @property
    def ip(self) -> Any: ...
    @property
    def with_hostmask(self) -> Any: ...
    @property
    def with_netmask(self) -> Any: ...
    @property
    def with_prefixlen(self) -> Any: ...

class IPv4Network(ipaddress._BaseV4, ipaddress._BaseNetwork):
    class _address_class(ipaddress._BaseV4, ipaddress._BaseAddress):
        class _constants:
            _linklocal_network: ClassVar[ipaddress.IPv4Network] = ...
            _loopback_network: ClassVar[ipaddress.IPv4Network] = ...
            _multicast_network: ClassVar[ipaddress.IPv4Network] = ...
            _private_networks: ClassVar[list] = ...
            _public_network: ClassVar[ipaddress.IPv4Network] = ...
            _reserved_network: ClassVar[ipaddress.IPv4Network] = ...
            _unspecified_address: ClassVar[ipaddress.IPv4Address] = ...
        __init__: ClassVar[function] = ...
        _ip: ClassVar[member_descriptor] = ...
        __slots__: ClassVar[tuple] = ...
        @property
        def is_global(self) -> Any: ...
        @property
        def is_link_local(self) -> Any: ...
        @property
        def is_loopback(self) -> Any: ...
        @property
        def is_multicast(self) -> Any: ...
        @property
        def is_private(self) -> Any: ...
        @property
        def is_reserved(self) -> Any: ...
        @property
        def is_unspecified(self) -> Any: ...
        @property
        def packed(self) -> Any: ...
    __init__: ClassVar[function] = ...
    @property
    def is_global(self) -> Any: ...

class IPv6Address(ipaddress._BaseV6, ipaddress._BaseAddress):
    class _constants:
        _linklocal_network: ClassVar[ipaddress.IPv6Network] = ...
        _multicast_network: ClassVar[ipaddress.IPv6Network] = ...
        _private_networks: ClassVar[list] = ...
        _reserved_networks: ClassVar[list] = ...
        _sitelocal_network: ClassVar[ipaddress.IPv6Network] = ...
    __init__: ClassVar[function] = ...
    _ip: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    @property
    def ipv4_mapped(self) -> Any: ...
    @property
    def is_global(self) -> Any: ...
    @property
    def is_link_local(self) -> Any: ...
    @property
    def is_loopback(self) -> Any: ...
    @property
    def is_multicast(self) -> Any: ...
    @property
    def is_private(self) -> Any: ...
    @property
    def is_reserved(self) -> Any: ...
    @property
    def is_site_local(self) -> Any: ...
    @property
    def is_unspecified(self) -> Any: ...
    @property
    def packed(self) -> Any: ...
    @property
    def sixtofour(self) -> Any: ...
    @property
    def teredo(self) -> Any: ...

class IPv6Interface(ipaddress.IPv6Address):
    __init__: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __hash__: ClassVar[function] = ...
    __lt__: ClassVar[function] = ...
    __reduce__: ClassVar[function] = ...
    def hostmask(self, *args, **kwargs) -> Any: ...
    @property
    def ip(self) -> Any: ...
    @property
    def is_loopback(self) -> Any: ...
    @property
    def is_unspecified(self) -> Any: ...
    @property
    def with_hostmask(self) -> Any: ...
    @property
    def with_netmask(self) -> Any: ...
    @property
    def with_prefixlen(self) -> Any: ...

class IPv6Network(ipaddress._BaseV6, ipaddress._BaseNetwork):
    class _address_class(ipaddress._BaseV6, ipaddress._BaseAddress):
        class _constants:
            _linklocal_network: ClassVar[ipaddress.IPv6Network] = ...
            _multicast_network: ClassVar[ipaddress.IPv6Network] = ...
            _private_networks: ClassVar[list] = ...
            _reserved_networks: ClassVar[list] = ...
            _sitelocal_network: ClassVar[ipaddress.IPv6Network] = ...
        __init__: ClassVar[function] = ...
        _ip: ClassVar[member_descriptor] = ...
        __slots__: ClassVar[tuple] = ...
        @property
        def ipv4_mapped(self) -> Any: ...
        @property
        def is_global(self) -> Any: ...
        @property
        def is_link_local(self) -> Any: ...
        @property
        def is_loopback(self) -> Any: ...
        @property
        def is_multicast(self) -> Any: ...
        @property
        def is_private(self) -> Any: ...
        @property
        def is_reserved(self) -> Any: ...
        @property
        def is_site_local(self) -> Any: ...
        @property
        def is_unspecified(self) -> Any: ...
        @property
        def packed(self) -> Any: ...
        @property
        def sixtofour(self) -> Any: ...
        @property
        def teredo(self) -> Any: ...
    __init__: ClassVar[function] = ...
    hosts: ClassVar[function] = ...
    @property
    def is_site_local(self) -> Any: ...

class ModelField(pydantic.utils.Representation):
    alias: ClassVar[member_descriptor] = ...
    allow_none: ClassVar[member_descriptor] = ...
    class_validators: ClassVar[member_descriptor] = ...
    default: ClassVar[member_descriptor] = ...
    default_factory: ClassVar[member_descriptor] = ...
    field_info: ClassVar[member_descriptor] = ...
    has_alias: ClassVar[member_descriptor] = ...
    key_field: ClassVar[member_descriptor] = ...
    model_config: ClassVar[member_descriptor] = ...
    name: ClassVar[member_descriptor] = ...
    outer_type_: ClassVar[member_descriptor] = ...
    parse_json: ClassVar[member_descriptor] = ...
    post_validators: ClassVar[member_descriptor] = ...
    pre_validators: ClassVar[member_descriptor] = ...
    required: ClassVar[member_descriptor] = ...
    shape: ClassVar[member_descriptor] = ...
    sub_fields: ClassVar[member_descriptor] = ...
    type_: ClassVar[member_descriptor] = ...
    validate_always: ClassVar[member_descriptor] = ...
    validators: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _apply_validators(self, *args, **kwargs) -> Any: ...
    def _create_sub_type(self, *args, **kwargs) -> Any: ...
    def _get_field_info(self, *args, **kwargs) -> Any: ...
    def _get_mapping_value(self, *args, **kwargs) -> Any: ...
    def _set_default_and_type(self, *args, **kwargs) -> Any: ...
    def _type_analysis(self, *args, **kwargs) -> Any: ...
    def _type_display(self, *args, **kwargs) -> Any: ...
    def _validate_iterable(self, *args, **kwargs) -> Any: ...
    def _validate_mapping_like(self, *args, **kwargs) -> Any: ...
    def _validate_sequence_like(self, *args, **kwargs) -> Any: ...
    def _validate_singleton(self, *args, **kwargs) -> Any: ...
    def _validate_tuple(self, *args, **kwargs) -> Any: ...
    def get_default(self, *args, **kwargs) -> Any: ...
    @classmethod
    def infer(self, *args, **kwargs) -> Any: ...
    def is_complex(self, *args, **kwargs) -> Any: ...
    def populate_validators(self, *args, **kwargs) -> Any: ...
    def prepare(self, *args, **kwargs) -> Any: ...
    def set_config(self, *args, **kwargs) -> Any: ...
    def validate(self, *args, **kwargs) -> Any: ...
    def __repr_args__(self, *args, **kwargs) -> Any: ...
    @property
    def alt_alias(self) -> Any: ...

class Path(pathlib.PurePath):
    _accessor: ClassVar[member_descriptor] = ...
    _closed: ClassVar[member_descriptor] = ...
    _init: ClassVar[function] = ...
    _make_child_relpath: ClassVar[function] = ...
    _opener: ClassVar[function] = ...
    _raise_closed: ClassVar[function] = ...
    _raw_open: ClassVar[function] = ...
    absolute: ClassVar[function] = ...
    chmod: ClassVar[function] = ...
    exists: ClassVar[function] = ...
    expanduser: ClassVar[function] = ...
    glob: ClassVar[function] = ...
    group: ClassVar[function] = ...
    is_block_device: ClassVar[function] = ...
    is_char_device: ClassVar[function] = ...
    is_dir: ClassVar[function] = ...
    is_fifo: ClassVar[function] = ...
    is_file: ClassVar[function] = ...
    is_mount: ClassVar[function] = ...
    is_socket: ClassVar[function] = ...
    is_symlink: ClassVar[function] = ...
    iterdir: ClassVar[function] = ...
    lchmod: ClassVar[function] = ...
    link_to: ClassVar[function] = ...
    lstat: ClassVar[function] = ...
    mkdir: ClassVar[function] = ...
    open: ClassVar[function] = ...
    owner: ClassVar[function] = ...
    read_bytes: ClassVar[function] = ...
    read_text: ClassVar[function] = ...
    rename: ClassVar[function] = ...
    replace: ClassVar[function] = ...
    resolve: ClassVar[function] = ...
    rglob: ClassVar[function] = ...
    rmdir: ClassVar[function] = ...
    samefile: ClassVar[function] = ...
    stat: ClassVar[function] = ...
    symlink_to: ClassVar[function] = ...
    touch: ClassVar[function] = ...
    unlink: ClassVar[function] = ...
    write_bytes: ClassVar[function] = ...
    write_text: ClassVar[function] = ...
    __enter__: ClassVar[function] = ...
    __exit__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def cwd(self, *args, **kwargs) -> Any: ...
    @classmethod
    def home(self, *args, **kwargs) -> Any: ...

class SecretBytes:
    max_length: ClassVar[None] = ...
    min_length: ClassVar[None] = ...
    __hash__: ClassVar[None] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, *args, **kwargs) -> Any: ...
    def get_secret_value(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    def __len__(self) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class SecretStr:
    max_length: ClassVar[None] = ...
    min_length: ClassVar[None] = ...
    __hash__: ClassVar[None] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def display(self, *args, **kwargs) -> Any: ...
    def get_secret_value(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    def __len__(self) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class SkipField(Exception):
    def __init__(self, *args, **kwargs) -> None: ...

class TypeVar(typing._Final, typing._Immutable):
    __init__: ClassVar[function] = ...
    __bound__: ClassVar[member_descriptor] = ...
    __constraints__: ClassVar[member_descriptor] = ...
    __contravariant__: ClassVar[member_descriptor] = ...
    __covariant__: ClassVar[member_descriptor] = ...
    __name__: ClassVar[member_descriptor] = ...
    __reduce__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...

class UUID:
    __init__: ClassVar[function] = ...
    int: ClassVar[member_descriptor] = ...
    is_safe: ClassVar[member_descriptor] = ...
    __eq__: ClassVar[function] = ...
    __ge__: ClassVar[function] = ...
    __getstate__: ClassVar[function] = ...
    __gt__: ClassVar[function] = ...
    __hash__: ClassVar[function] = ...
    __int__: ClassVar[function] = ...
    __le__: ClassVar[function] = ...
    __lt__: ClassVar[function] = ...
    __setattr__: ClassVar[function] = ...
    __setstate__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...
    @property
    def bytes(self) -> Any: ...
    @property
    def bytes_le(self) -> Any: ...
    @property
    def clock_seq(self) -> Any: ...
    @property
    def clock_seq_hi_variant(self) -> Any: ...
    @property
    def clock_seq_low(self) -> Any: ...
    @property
    def fields(self) -> Any: ...
    @property
    def hex(self) -> Any: ...
    @property
    def node(self) -> Any: ...
    @property
    def time(self) -> Any: ...
    @property
    def time_hi_version(self) -> Any: ...
    @property
    def time_low(self) -> Any: ...
    @property
    def time_mid(self) -> Any: ...
    @property
    def urn(self) -> Any: ...
    @property
    def variant(self) -> Any: ...
    @property
    def version(self) -> Any: ...

class date:
    day: ClassVar[getset_descriptor] = ...
    max: ClassVar[datetime.date] = ...
    min: ClassVar[datetime.date] = ...
    month: ClassVar[getset_descriptor] = ...
    resolution: ClassVar[datetime.timedelta] = ...
    year: ClassVar[getset_descriptor] = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def ctime() -> Any: ...
    @classmethod
    def fromisocalendar(self, *args, **kwargs) -> Any: ...
    @classmethod
    def fromisoformat(self, *args, **kwargs) -> Any: ...
    @classmethod
    def fromordinal(self, *args, **kwargs) -> Any: ...
    @classmethod
    def fromtimestamp(self, *args, **kwargs) -> Any: ...
    def isocalendar(self, *args, **kwargs) -> Any: ...
    def isoformat(self, *args, **kwargs) -> Any: ...
    def isoweekday(self, *args, **kwargs) -> Any: ...
    def replace(self, *args, **kwargs) -> Any: ...
    def strftime(self, *args, **kwargs) -> Any: ...
    def timetuple(self, *args, **kwargs) -> Any: ...
    @classmethod
    def today(self, *args, **kwargs) -> Any: ...
    def toordinal(self, *args, **kwargs) -> Any: ...
    def weekday(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __format__(self, *args, **kwargs) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...

class datetime(datetime.date):
    fold: ClassVar[getset_descriptor] = ...
    hour: ClassVar[getset_descriptor] = ...
    max: ClassVar[datetime.datetime] = ...
    microsecond: ClassVar[getset_descriptor] = ...
    min: ClassVar[datetime.datetime] = ...
    minute: ClassVar[getset_descriptor] = ...
    resolution: ClassVar[datetime.timedelta] = ...
    second: ClassVar[getset_descriptor] = ...
    tzinfo: ClassVar[getset_descriptor] = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def astimezone(self, *args, **kwargs) -> Any: ...
    @classmethod
    def combine(self, *args, **kwargs) -> Any: ...
    def ctime() -> Any: ...
    def date(self, *args, **kwargs) -> Any: ...
    def dst(self) -> Any: ...
    @classmethod
    def fromisoformat(self, *args, **kwargs) -> Any: ...
    @classmethod
    def fromtimestamp(self, *args, **kwargs) -> Any: ...
    def isoformat(self, *args, **kwargs) -> Any: ...
    @classmethod
    def now(self, *args, **kwargs) -> Any: ...
    def replace(self, *args, **kwargs) -> Any: ...
    @classmethod
    def strptime(self, *args, **kwargs) -> Any: ...
    def time(self, *args, **kwargs) -> Any: ...
    def timestamp(self, *args, **kwargs) -> Any: ...
    def timetuple(self, *args, **kwargs) -> Any: ...
    def timetz(self, *args, **kwargs) -> Any: ...
    def tzname(self) -> Any: ...
    @classmethod
    def utcfromtimestamp(self, *args, **kwargs) -> Any: ...
    @classmethod
    def utcnow(self, *args, **kwargs) -> Any: ...
    def utcoffset(self) -> Any: ...
    def utctimetuple(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __reduce_ex__(self, protocol) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...

class defaultdict(dict):
    default_factory: ClassVar[member_descriptor] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def __copy__(self) -> Any: ...
    def __missing__(key) -> Any: ...
    def __reduce__(self) -> Any: ...

class time:
    fold: ClassVar[getset_descriptor] = ...
    hour: ClassVar[getset_descriptor] = ...
    max: ClassVar[datetime.time] = ...
    microsecond: ClassVar[getset_descriptor] = ...
    min: ClassVar[datetime.time] = ...
    minute: ClassVar[getset_descriptor] = ...
    resolution: ClassVar[datetime.timedelta] = ...
    second: ClassVar[getset_descriptor] = ...
    tzinfo: ClassVar[getset_descriptor] = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def dst(self) -> Any: ...
    @classmethod
    def fromisoformat(self, *args, **kwargs) -> Any: ...
    def isoformat(self, *args, **kwargs) -> Any: ...
    def replace(self, *args, **kwargs) -> Any: ...
    def strftime(self, *args, **kwargs) -> Any: ...
    def tzname(self) -> Any: ...
    def utcoffset(self) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __format__(self, *args, **kwargs) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __reduce_ex__(self, protocol) -> Any: ...

class timedelta:
    days: ClassVar[member_descriptor] = ...
    max: ClassVar[datetime.timedelta] = ...
    microseconds: ClassVar[member_descriptor] = ...
    min: ClassVar[datetime.timedelta] = ...
    resolution: ClassVar[datetime.timedelta] = ...
    seconds: ClassVar[member_descriptor] = ...
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def total_seconds(self, *args, **kwargs) -> Any: ...
    def __abs__(self) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    def __divmod__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __floordiv__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mod__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __neg__(self) -> Any: ...
    def __pos__(self) -> Any: ...
    def __radd__(self, other) -> Any: ...
    def __rdivmod__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __rfloordiv__(self, other) -> Any: ...
    def __rmod__(self, other) -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __rsub__(self, other) -> Any: ...
    def __rtruediv__(self, other) -> Any: ...
    def __sub__(self, other) -> Any: ...
    def __truediv__(self, other) -> Any: ...