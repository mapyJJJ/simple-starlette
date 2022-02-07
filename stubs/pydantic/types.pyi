from typing import Any, Callable, ClassVar, Dict, List, Optional, Tuple, Union

import _weakrefset
import decimal
import enum
import pathlib
import re
import typing
import uuid
Any: typing._SpecialForm
BYTE_SIZES: dict
Callable: typing._VariadicGenericAlias
ClassVar: typing._SpecialForm
Dict: typing._GenericAlias
List: typing._GenericAlias
NoneBytes: typing._GenericAlias
NoneStr: typing._GenericAlias
NoneStrBytes: typing._GenericAlias
Optional: typing._SpecialForm
OptionalInt: typing._GenericAlias
OptionalIntFloat: typing._GenericAlias
OptionalIntFloatDecimal: typing._GenericAlias
Pattern: typing._GenericAlias
Set: typing._GenericAlias
StrBytes: typing._GenericAlias
StrIntFloat: typing._GenericAlias
T: typing.TypeVar
TYPE_CHECKING: bool
Tuple: typing._VariadicGenericAlias
Type: typing._GenericAlias
Union: typing._SpecialForm
_DEFINED_TYPES: _weakrefset.WeakSet
_registered: cython_function_or_method
byte_string_re: re.Pattern
bytes_validator: cython_function_or_method
cast: function
conbytes: cython_function_or_method
condecimal: cython_function_or_method
confloat: cython_function_or_method
conint: cython_function_or_method
conlist: cython_function_or_method
conset: cython_function_or_method
constr: cython_function_or_method
constr_length_validator: cython_function_or_method
constr_lower: cython_function_or_method
constr_strip_whitespace: cython_function_or_method
decimal_validator: cython_function_or_method
float_validator: cython_function_or_method
import_string: cython_function_or_method
int_validator: cython_function_or_method
list_validator: cython_function_or_method
new_class: function
number_multiple_validator: cython_function_or_method
number_size_validator: cython_function_or_method
overload: function
path_exists_validator: cython_function_or_method
path_validator: cython_function_or_method
set_validator: cython_function_or_method
str_validator: cython_function_or_method
strict_bytes_validator: cython_function_or_method
strict_float_validator: cython_function_or_method
strict_int_validator: cython_function_or_method
strict_str_validator: cython_function_or_method
update_not_none: cython_function_or_method

class ByteSize(int):
    def human_readable(self, *args, **kwargs) -> Any: ...
    def to(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...

class ConstrainedBytes(bytes):
    max_length: ClassVar[None] = ...
    min_length: ClassVar[None] = ...
    strict: ClassVar[bool] = ...
    strip_whitespace: ClassVar[bool] = ...
    to_lower: ClassVar[bool] = ...
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

class ConstrainedNumberMeta(type):
    def __init__(self, *args, **kwargs) -> None: ...

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

class DirectoryPath(pathlib.Path):
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

class FilePath(pathlib.Path):
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class Json:
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class JsonMeta(type):
    def __getitem__(self, index) -> Any: ...

class JsonWrapper: ...

class NegativeFloat(ConstrainedFloat):
    lt: ClassVar[int] = ...

class NegativeInt(ConstrainedInt):
    lt: ClassVar[int] = ...

class NonNegativeFloat(ConstrainedFloat):
    ge: ClassVar[int] = ...

class NonNegativeInt(ConstrainedInt):
    ge: ClassVar[int] = ...

class NonPositiveFloat(ConstrainedFloat):
    le: ClassVar[int] = ...

class NonPositiveInt(ConstrainedInt):
    le: ClassVar[int] = ...

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

class PaymentCardBrand(str, enum.Enum):
    class _member_type_:
        @classmethod
        def __init__(self, *args, **kwargs) -> None: ...
        def capitalize(self, *args, **kwargs) -> Any: ...
        def casefold(self, *args, **kwargs) -> Any: ...
        def center(self, *args, **kwargs) -> Any: ...
        def count(self, *args, **kwargs) -> Any: ...
        def encode(self, *args, **kwargs) -> Any: ...
        def endswith(self, *args, **kwargs) -> Any: ...
        def expandtabs(self, *args, **kwargs) -> Any: ...
        def find(self, *args, **kwargs) -> Any: ...
        def format(*args, **kwargs) -> str: ...
        def format_map(mapping) -> str: ...
        def index(self, *args, **kwargs) -> Any: ...
        def isalnum(self, *args, **kwargs) -> Any: ...
        def isalpha(self, *args, **kwargs) -> Any: ...
        def isascii(self, *args, **kwargs) -> Any: ...
        def isdecimal(self, *args, **kwargs) -> Any: ...
        def isdigit(self, *args, **kwargs) -> Any: ...
        def isidentifier(self, *args, **kwargs) -> Any: ...
        def islower(self, *args, **kwargs) -> Any: ...
        def isnumeric(self, *args, **kwargs) -> Any: ...
        def isprintable(self, *args, **kwargs) -> Any: ...
        def isspace(self, *args, **kwargs) -> Any: ...
        def istitle(self, *args, **kwargs) -> Any: ...
        def isupper(self, *args, **kwargs) -> Any: ...
        def join(self, *args, **kwargs) -> Any: ...
        def ljust(self, *args, **kwargs) -> Any: ...
        def lower(self, *args, **kwargs) -> Any: ...
        def lstrip(self, *args, **kwargs) -> Any: ...
        def maketrans(self, *args, **kwargs) -> Any: ...
        def partition(self, *args, **kwargs) -> Any: ...
        def replace(self, *args, **kwargs) -> Any: ...
        def rfind(self, *args, **kwargs) -> Any: ...
        def rindex(self, *args, **kwargs) -> Any: ...
        def rjust(self, *args, **kwargs) -> Any: ...
        def rpartition(self, *args, **kwargs) -> Any: ...
        def rsplit(self, *args, **kwargs) -> Any: ...
        def rstrip(self, *args, **kwargs) -> Any: ...
        def split(self, *args, **kwargs) -> Any: ...
        def splitlines(self, *args, **kwargs) -> Any: ...
        def startswith(self, *args, **kwargs) -> Any: ...
        def strip(self, *args, **kwargs) -> Any: ...
        def swapcase(self, *args, **kwargs) -> Any: ...
        def title(self, *args, **kwargs) -> Any: ...
        def translate(self, *args, **kwargs) -> Any: ...
        def upper(self, *args, **kwargs) -> Any: ...
        def zfill(self, *args, **kwargs) -> Any: ...
        def __add__(self, other) -> Any: ...
        def __contains__(self, other) -> Any: ...
        def __eq__(self, other) -> Any: ...
        def __format__(self, *args, **kwargs) -> Any: ...
        def __ge__(self, other) -> Any: ...
        def __getitem__(self, index) -> Any: ...
        def __getnewargs__(self, *args, **kwargs) -> Any: ...
        def __gt__(self, other) -> Any: ...
        def __hash__(self) -> Any: ...
        def __iter__(self) -> Any: ...
        def __le__(self, other) -> Any: ...
        def __len__(self) -> Any: ...
        def __lt__(self, other) -> Any: ...
        def __mod__(self, other) -> Any: ...
        def __mul__(self, other) -> Any: ...
        def __ne__(self, other) -> Any: ...
        def __rmod__(self, other) -> Any: ...
        def __rmul__(self, other) -> Any: ...
        def __sizeof__(self) -> Any: ...
    __new__: ClassVar[function] = ...
    _generate_next_value_: ClassVar[function] = ...
    _member_map_: ClassVar[dict] = ...
    _member_names_: ClassVar[list] = ...
    _value2member_map_: ClassVar[dict] = ...
    amex: ClassVar[PaymentCardBrand] = ...
    mastercard: ClassVar[PaymentCardBrand] = ...
    other: ClassVar[PaymentCardBrand] = ...
    visa: ClassVar[PaymentCardBrand] = ...
    __format__: ClassVar[function] = ...

class PaymentCardNumber(str):
    max_length: ClassVar[int] = ...
    min_length: ClassVar[int] = ...
    strip_whitespace: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _get_brand(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate_digits(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate_length_for_brand(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate_luhn_check_digit(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @property
    def masked(self) -> Any: ...

class PositiveFloat(ConstrainedFloat):
    gt: ClassVar[int] = ...

class PositiveInt(ConstrainedInt):
    gt: ClassVar[int] = ...

class PyObject:
    validate_always: ClassVar[bool] = ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...

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

class StrictBool(int):
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class StrictBytes(ConstrainedBytes):
    strict: ClassVar[bool] = ...

class StrictFloat(ConstrainedFloat):
    strict: ClassVar[bool] = ...

class StrictInt(ConstrainedInt):
    strict: ClassVar[bool] = ...

class StrictStr(ConstrainedStr):
    strict: ClassVar[bool] = ...

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

class UUID1(uuid.UUID):
    _required_version: ClassVar[int] = ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...

class UUID3(UUID1):
    _required_version: ClassVar[int] = ...

class UUID4(UUID1):
    _required_version: ClassVar[int] = ...

class UUID5(UUID1):
    _required_version: ClassVar[int] = ...

class WeakSet:
    __init__: ClassVar[function] = ...
    _commit_removals: ClassVar[function] = ...
    add: ClassVar[function] = ...
    clear: ClassVar[function] = ...
    copy: ClassVar[function] = ...
    difference: ClassVar[function] = ...
    difference_update: ClassVar[function] = ...
    discard: ClassVar[function] = ...
    intersection: ClassVar[function] = ...
    intersection_update: ClassVar[function] = ...
    isdisjoint: ClassVar[function] = ...
    issubset: ClassVar[function] = ...
    issuperset: ClassVar[function] = ...
    pop: ClassVar[function] = ...
    remove: ClassVar[function] = ...
    symmetric_difference: ClassVar[function] = ...
    symmetric_difference_update: ClassVar[function] = ...
    union: ClassVar[function] = ...
    update: ClassVar[function] = ...
    __and__: ClassVar[function] = ...
    __contains__: ClassVar[function] = ...
    __eq__: ClassVar[function] = ...
    __ge__: ClassVar[function] = ...
    __gt__: ClassVar[function] = ...
    __hash__: ClassVar[None] = ...
    __iand__: ClassVar[function] = ...
    __ior__: ClassVar[function] = ...
    __isub__: ClassVar[function] = ...
    __iter__: ClassVar[function] = ...
    __ixor__: ClassVar[function] = ...
    __le__: ClassVar[function] = ...
    __len__: ClassVar[function] = ...
    __lt__: ClassVar[function] = ...
    __or__: ClassVar[function] = ...
    __reduce__: ClassVar[function] = ...
    __sub__: ClassVar[function] = ...
    __xor__: ClassVar[function] = ...
