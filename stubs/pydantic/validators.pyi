from typing import Any, Callable, ClassVar, Dict, List, Tuple, Union

from typing import overload
import datetime
import enum
import ipaddress
import pathlib
import typing
Any: typing._SpecialForm
AnyCallable: typing._GenericAlias
BOOL_FALSE: set
BOOL_TRUE: set
Callable: typing._VariadicGenericAlias
Deque: typing._GenericAlias
Dict: typing._GenericAlias
FrozenSet: typing._GenericAlias
Generator: typing._GenericAlias
List: typing._GenericAlias
Literal: typing._SpecialForm
NONE_TYPES: set
NamedTupleT: typing.TypeVar
Pattern: typing._GenericAlias
Set: typing._GenericAlias
T: typing.TypeVar
TYPE_CHECKING: bool
Tuple: typing._VariadicGenericAlias
Type: typing._GenericAlias
Union: typing._SpecialForm
_VALIDATORS: list
all_literal_values: cython_function_or_method
almost_equal_floats: cython_function_or_method
any_class_validator: cython_function_or_method
anystr_length_validator: cython_function_or_method
anystr_lower: cython_function_or_method
anystr_strip_whitespace: cython_function_or_method
bool_validator: cython_function_or_method
bytes_validator: cython_function_or_method
callable_validator: cython_function_or_method
constant_validator: cython_function_or_method
constr_length_validator: cython_function_or_method
constr_lower: cython_function_or_method
constr_strip_whitespace: cython_function_or_method
decimal_validator: cython_function_or_method
deque_validator: cython_function_or_method
dict_validator: cython_function_or_method
display_as_type: cython_function_or_method
enum_member_validator: cython_function_or_method
enum_validator: cython_function_or_method
find_validators: cython_function_or_method
float_validator: cython_function_or_method
frozenset_validator: cython_function_or_method
get_class: cython_function_or_method
hashable_validator: cython_function_or_method
int_enum_validator: cython_function_or_method
int_validator: cython_function_or_method
ip_v4_address_validator: cython_function_or_method
ip_v4_interface_validator: cython_function_or_method
ip_v4_network_validator: cython_function_or_method
ip_v6_address_validator: cython_function_or_method
ip_v6_interface_validator: cython_function_or_method
ip_v6_network_validator: cython_function_or_method
is_callable_type: cython_function_or_method
is_literal_type: cython_function_or_method
is_namedtuple: cython_function_or_method
is_typeddict: cython_function_or_method
lenient_issubclass: cython_function_or_method
list_validator: cython_function_or_method
make_arbitrary_type_validator: cython_function_or_method
make_class_validator: cython_function_or_method
make_literal_validator: cython_function_or_method
make_namedtuple_validator: cython_function_or_method
make_typeddict_validator: cython_function_or_method
none_validator: cython_function_or_method
number_multiple_validator: cython_function_or_method
number_size_validator: cython_function_or_method
ordered_dict_validator: cython_function_or_method
parse_date: cython_function_or_method
parse_datetime: cython_function_or_method
parse_duration: cython_function_or_method
parse_time: cython_function_or_method
path_exists_validator: cython_function_or_method
path_validator: cython_function_or_method
pattern_validator: cython_function_or_method
sequence_like: cython_function_or_method
set_validator: cython_function_or_method
str_validator: cython_function_or_method
strict_bytes_validator: cython_function_or_method
strict_float_validator: cython_function_or_method
strict_int_validator: cython_function_or_method
strict_str_validator: cython_function_or_method
tuple_validator: cython_function_or_method
uuid_validator: cython_function_or_method
validate_json: cython_function_or_method

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

class DecimalException(ArithmeticError): ...

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

class Hashable:
    _abc_impl: ClassVar[_abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    __hash__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...
    @classmethod
    def __subclasshook__(self, *args, **kwargs) -> Any: ...

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

class IfConfig:
    def __init__(self, *args, **kwargs) -> None: ...
    def check(self, *args, **kwargs) -> Any: ...

class IntEnum(int, enum.Enum):
    class _member_type_:
        denominator: ClassVar[getset_descriptor] = ...
        imag: ClassVar[getset_descriptor] = ...
        numerator: ClassVar[getset_descriptor] = ...
        real: ClassVar[getset_descriptor] = ...
        @classmethod
        def __init__(self, *args, **kwargs) -> None: ...
        @overload
        def as_integer_ratio() -> Any: ...
        @overload
        def as_integer_ratio() -> Any: ...
        @overload
        def as_integer_ratio() -> Any: ...
        def bit_length() -> Any: ...
        def conjugate(self, *args, **kwargs) -> Any: ...
        @classmethod
        def from_bytes(self, *args, **kwargs) -> Any: ...
        def to_bytes(self, *args, **kwargs) -> Any: ...
        def __abs__(self) -> Any: ...
        def __add__(self, other) -> Any: ...
        def __and__(self, other) -> Any: ...
        def __bool__(self) -> Any: ...
        def __ceil__(self, *args, **kwargs) -> Any: ...
        def __divmod__(self, other) -> Any: ...
        def __eq__(self, other) -> Any: ...
        def __float__(self) -> Any: ...
        def __floor__(self, *args, **kwargs) -> Any: ...
        def __floordiv__(self, other) -> Any: ...
        def __format__(self, *args, **kwargs) -> Any: ...
        def __ge__(self, other) -> Any: ...
        def __getnewargs__(self, *args, **kwargs) -> Any: ...
        def __gt__(self, other) -> Any: ...
        def __hash__(self) -> Any: ...
        def __index__(self) -> Any: ...
        def __int__(self) -> Any: ...
        def __invert__(self) -> Any: ...
        def __le__(self, other) -> Any: ...
        def __lshift__(self, other) -> Any: ...
        def __lt__(self, other) -> Any: ...
        def __mod__(self, other) -> Any: ...
        def __mul__(self, other) -> Any: ...
        def __ne__(self, other) -> Any: ...
        def __neg__(self) -> Any: ...
        def __or__(self, other) -> Any: ...
        def __pos__(self) -> Any: ...
        def __pow__(self, other) -> Any: ...
        def __radd__(self, other) -> Any: ...
        def __rand__(self, other) -> Any: ...
        def __rdivmod__(self, other) -> Any: ...
        def __rfloordiv__(self, other) -> Any: ...
        def __rlshift__(self, other) -> Any: ...
        def __rmod__(self, other) -> Any: ...
        def __rmul__(self, other) -> Any: ...
        def __ror__(self, other) -> Any: ...
        def __round__(self) -> Any: ...
        def __rpow__(self, other) -> Any: ...
        def __rrshift__(self, other) -> Any: ...
        def __rshift__(self, other) -> Any: ...
        def __rsub__(self, other) -> Any: ...
        def __rtruediv__(self, other) -> Any: ...
        def __rxor__(self, other) -> Any: ...
        def __sizeof__(self) -> Any: ...
        def __sub__(self, other) -> Any: ...
        def __truediv__(self, other) -> Any: ...
        def __trunc__(self) -> Any: ...
        def __xor__(self, other) -> Any: ...
    __new__: ClassVar[function] = ...
    _generate_next_value_: ClassVar[function] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _value2member_map_: ClassVar[dict] = ...
    __format__: ClassVar[function] = ...

class NamedTuple:
    _root: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...

class OrderedDict(dict):
    __hash__: ClassVar[None] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def copy() -> ashallowcopyofod: ...
    @classmethod
    def fromkeys(self, *args, **kwargs) -> Any: ...
    def items(self, *args, **kwargs) -> Any: ...
    def keys(self, *args, **kwargs) -> Any: ...
    def move_to_end(self, *args, **kwargs) -> Any: ...
    def pop(self, *args, **kwargs) -> Any: ...
    def popitem(self, *args, **kwargs) -> Any: ...
    def setdefault(self, *args, **kwargs) -> Any: ...
    def update(self, *args, **kwargs) -> Any: ...
    def values(self, *args, **kwargs) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __reversed__() -> Any: ...
    def __setitem__(self, index, object) -> Any: ...
    def __sizeof__(self) -> Any: ...

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

class deque:
    maxlen: ClassVar[getset_descriptor] = ...
    __hash__: ClassVar[None] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def append(self, *args, **kwargs) -> Any: ...
    def appendleft(self, *args, **kwargs) -> Any: ...
    def clear(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def count(self, *args, **kwargs) -> Any: ...
    def extend(self, *args, **kwargs) -> Any: ...
    def extendleft(self, *args, **kwargs) -> Any: ...
    def index(self, *args, **kwargs) -> Any: ...
    def insert(index, object) -> Any: ...
    def pop(self, *args, **kwargs) -> Any: ...
    def popleft(self, *args, **kwargs) -> Any: ...
    def remove(value) -> Any: ...
    def reverse() -> Any: ...
    def rotate(self, *args, **kwargs) -> Any: ...
    def __add__(self, other) -> Any: ...
    def __bool__(self) -> Any: ...
    def __contains__(self, other) -> Any: ...
    def __copy__(self) -> Any: ...
    def __delitem__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __getitem__(self, index) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __iadd__(self, other) -> Any: ...
    def __imul__(self, other) -> Any: ...
    def __iter__(self) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __len__(self) -> Any: ...
    def __lt__(self, other) -> Any: ...
    def __mul__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __reduce__(self) -> Any: ...
    def __reversed__() -> Any: ...
    def __rmul__(self, other) -> Any: ...
    def __setitem__(self, index, object) -> Any: ...
    def __sizeof__() -> Any: ...

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
