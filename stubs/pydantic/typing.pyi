from typing import Any, Callable, ClassVar, Dict, List, Optional, Tuple, Union

import typing
AbstractSet: typing._GenericAlias
AnnotatedTypeNames: set
Any: typing._SpecialForm
AnyCallable: typing._GenericAlias
ClassVar: typing._SpecialForm
Dict: typing._GenericAlias
Generator: typing._GenericAlias
GenericAlias: tuple
List: typing._GenericAlias
Literal: typing._SpecialForm
Mapping: typing._GenericAlias
NONE_TYPES: set
NewType: function
NoArgAnyCallable: typing._GenericAlias
Optional: typing._SpecialForm
Sequence: typing._GenericAlias
Set: typing._GenericAlias
TYPE_CHECKING: bool
Tuple: typing._VariadicGenericAlias
Type: typing._GenericAlias
TypingCallable: typing._VariadicGenericAlias
Union: typing._SpecialForm
_check_classvar: cython_function_or_method
_eval_type: function
_generic_get_args: cython_function_or_method
_typing_get_args: function
_typing_get_origin: function
all_literal_values: cython_function_or_method
cast: function
display_as_type: cython_function_or_method
evaluate_forwardref: cython_function_or_method
get_all_type_hints: function
get_args: cython_function_or_method
get_class: cython_function_or_method
get_origin: cython_function_or_method
get_type_hints: function
is_callable_type: cython_function_or_method
is_classvar: cython_function_or_method
is_literal_type: cython_function_or_method
is_namedtuple: cython_function_or_method
is_new_type: cython_function_or_method
is_typeddict: cython_function_or_method
literal_values: cython_function_or_method
new_type_supertype: cython_function_or_method
resolve_annotations: cython_function_or_method
test_type: function
update_field_forward_refs: cython_function_or_method

class Annotated:
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def __class_getitem__(self, *args, **kwargs) -> Any: ...
    @classmethod
    def __init_subclass__(self, *args, **kwargs) -> Any: ...

class Callable:
    _abc_impl: ClassVar[_abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    __call__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...
    @classmethod
    def __subclasshook__(self, *args, **kwargs) -> Any: ...

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

class NoneType:
    @classmethod
    def __init__(self, *args, **kwargs) -> None: ...
    def __bool__(self) -> Any: ...

class typing_base:
    __slots__: ClassVar[tuple] = ...
    @classmethod
    def __init_subclass__(self, *args, **kwargs) -> Any: ...
