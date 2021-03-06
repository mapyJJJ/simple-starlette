from typing import Any, Callable, ClassVar, Dict, Optional, Union

import pydantic.errors
import pydantic.fields
import pydantic.utils
import typing
Any: typing._SpecialForm
Callable: typing._VariadicGenericAlias
Dict: typing._GenericAlias
Field: cython_function_or_method
Optional: typing._SpecialForm
Required: ellipsis
TYPE_CHECKING: bool
Type: typing._GenericAlias
Undefined: pydantic.fields.UndefinedType
Union: typing._SpecialForm
_generate_pydantic_post_init: cython_function_or_method
_get_validators: cython_function_or_method
_process_class: cython_function_or_method
_validate_dataclass: cython_function_or_method
create_model: cython_function_or_method
dataclass: cython_function_or_method
gather_all_validators: cython_function_or_method
is_builtin_dataclass: cython_function_or_method
make_dataclass_validator: cython_function_or_method
overload: function
resolve_annotations: cython_function_or_method
setattr_validate_assignment: cython_function_or_method
validate_model: cython_function_or_method

class ClassAttribute:
    name: ClassVar[member_descriptor] = ...
    value: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __get__(self, instance, owner) -> Any: ...

class DataclassTypeError(pydantic.errors.PydanticTypeError):
    code: ClassVar[str] = ...
    msg_template: ClassVar[str] = ...

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

class TypeVar(typing._Final, typing._Immutable):
    __init__: ClassVar[function] = ...
    __bound__: ClassVar[member_descriptor] = ...
    __constraints__: ClassVar[member_descriptor] = ...
    __contravariant__: ClassVar[member_descriptor] = ...
    __covariant__: ClassVar[member_descriptor] = ...
    __name__: ClassVar[member_descriptor] = ...
    __reduce__: ClassVar[function] = ...
    __slots__: ClassVar[tuple] = ...

class ValidationError(pydantic.utils.Representation, ValueError):
    _error_cache: ClassVar[member_descriptor] = ...
    model: ClassVar[member_descriptor] = ...
    raw_errors: ClassVar[member_descriptor] = ...
    __slots__: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def errors(self, *args, **kwargs) -> Any: ...
    def json(self, *args, **kwargs) -> Any: ...
    def __repr_args__(self, *args, **kwargs) -> Any: ...
