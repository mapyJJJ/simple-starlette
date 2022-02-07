from typing import Any, ClassVar, Dict, Optional, Tuple, Union

import pydantic.errors
import pydantic.utils
import typing
Any: typing._SpecialForm
COLORS_BY_NAME: dict
COLORS_BY_VALUE: dict
ColorTuple: typing._GenericAlias
ColorType: typing._GenericAlias
Dict: typing._GenericAlias
HslColorTuple: typing._GenericAlias
Optional: typing._SpecialForm
TYPE_CHECKING: bool
Tuple: typing._VariadicGenericAlias
Union: typing._SpecialForm
_r_255: str
_r_alpha: str
_r_comma: str
_r_h: str
_r_sl: str
almost_equal_floats: cython_function_or_method
cast: function
float_to_255: cython_function_or_method
hls_to_rgb: function
ints_to_rgba: cython_function_or_method
parse_color_value: cython_function_or_method
parse_float_alpha: cython_function_or_method
parse_hsl: cython_function_or_method
parse_str: cython_function_or_method
parse_tuple: cython_function_or_method
r_hex_long: str
r_hex_short: str
r_hsl: str
r_hsla: str
r_rgb: str
r_rgba: str
rads: float
repeat_colors: set
rgb_to_hls: function

class Color(pydantic.utils.Representation):
    _original: ClassVar[member_descriptor] = ...
    _rgba: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _alpha_float(self, *args, **kwargs) -> Any: ...
    def as_hex(self, *args, **kwargs) -> Any: ...
    def as_hsl(self, *args, **kwargs) -> Any: ...
    def as_hsl_tuple(self, *args, **kwargs) -> Any: ...
    def as_named(self, *args, **kwargs) -> Any: ...
    def as_rgb(self, *args, **kwargs) -> Any: ...
    def as_rgb_tuple(self, *args, **kwargs) -> Any: ...
    def original(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __modify_schema__(self, *args, **kwargs) -> Any: ...
    def __repr_args__(self, *args, **kwargs) -> Any: ...

class ColorError(pydantic.errors.PydanticValueError):
    msg_template: ClassVar[str] = ...

class RGBA:
    _tuple: ClassVar[member_descriptor] = ...
    alpha: ClassVar[member_descriptor] = ...
    b: ClassVar[member_descriptor] = ...
    g: ClassVar[member_descriptor] = ...
    r: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, index) -> Any: ...

class Representation:
    __slots__: ClassVar[tuple] = ...
    def __pretty__(self, *args, **kwargs) -> Any: ...
    def __repr_args__(self, *args, **kwargs) -> Any: ...
    def __repr_name__(self, *args, **kwargs) -> Any: ...
    def __repr_str__(self, *args, **kwargs) -> Any: ...