from typing import Any, ClassVar, Dict

import pydantic.main
import pydantic.utils
import typing
Any: typing._SpecialForm
Dict: typing._GenericAlias
FrozenSet: typing._GenericAlias
Required: ellipsis
TYPE_CHECKING: bool
Type: typing._GenericAlias
create_model: cython_function_or_method
create_model_from_namedtuple: cython_function_or_method
create_model_from_typeddict: cython_function_or_method

class BaseModel(pydantic.utils.Representation):
    class Config:
        class getter_dict(pydantic.utils.Representation):
            _obj: ClassVar[member_descriptor] = ...
            __hash__: ClassVar[None] = ...
            __slots__: ClassVar[tuple] = ...
            def __init__(self, *args, **kwargs) -> None: ...
            def extra_keys(self, *args, **kwargs) -> Any: ...
            def get(self, *args, **kwargs) -> Any: ...
            def items(self, *args, **kwargs) -> Any: ...
            def keys(self, *args, **kwargs) -> Any: ...
            def values(self, *args, **kwargs) -> Any: ...
            def __contains__(self, other) -> Any: ...
            def __eq__(self, other) -> Any: ...
            def __getitem__(self, index) -> Any: ...
            def __iter__(self) -> Any: ...
            def __len__(self) -> Any: ...
            def __repr_args__(self, *args, **kwargs) -> Any: ...
            def __repr_name__(self, *args, **kwargs) -> Any: ...
        alias_generator: ClassVar[None] = ...
        allow_mutation: ClassVar[bool] = ...
        allow_population_by_field_name: ClassVar[bool] = ...
        anystr_lower: ClassVar[bool] = ...
        anystr_strip_whitespace: ClassVar[bool] = ...
        arbitrary_types_allowed: ClassVar[bool] = ...
        copy_on_model_validation: ClassVar[bool] = ...
        error_msg_templates: ClassVar[dict] = ...
        extra: ClassVar[pydantic.main.Extra] = ...
        fields: ClassVar[dict] = ...
        frozen: ClassVar[bool] = ...
        json_dumps: ClassVar[function] = ...
        json_encoders: ClassVar[dict] = ...
        json_loads: ClassVar[function] = ...
        keep_untouched: ClassVar[tuple] = ...
        max_anystr_length: ClassVar[None] = ...
        min_anystr_length: ClassVar[None] = ...
        orm_mode: ClassVar[bool] = ...
        schema_extra: ClassVar[dict] = ...
        title: ClassVar[None] = ...
        underscore_attrs_are_private: ClassVar[bool] = ...
        use_enum_values: ClassVar[bool] = ...
        validate_all: ClassVar[bool] = ...
        validate_assignment: ClassVar[bool] = ...
        @classmethod
        def get_field_info(self, *args, **kwargs) -> Any: ...
        @classmethod
        def prepare_field(self, *args, **kwargs) -> Any: ...

    class __config__(pydantic.main.BaseConfig):
        json_encoders: ClassVar[dict] = ...
    _abc_impl: ClassVar[_abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    __class_vars__: ClassVar[set] = ...
    __custom_root_type__: ClassVar[bool] = ...
    __fields__: ClassVar[dict] = ...
    __fields_set__: ClassVar[member_descriptor] = ...
    __hash__: ClassVar[None] = ...
    __post_root_validators__: ClassVar[list] = ...
    __pre_root_validators__: ClassVar[list] = ...
    __private_attributes__: ClassVar[dict] = ...
    __schema_cache__: ClassVar[dict] = ...
    __slots__: ClassVar[set] = ...
    __validators__: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def _calculate_keys(self, *args, **kwargs) -> Any: ...
    @classmethod
    def _decompose_class(self, *args, **kwargs) -> Any: ...
    @classmethod
    def _enforce_dict_if_root(self, *args, **kwargs) -> Any: ...
    @classmethod
    def _get_value(self, *args, **kwargs) -> Any: ...
    def _init_private_attributes(self, *args, **kwargs) -> Any: ...
    def _iter(self, *args, **kwargs) -> Any: ...
    @classmethod
    def construct(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def dict(self, *args, **kwargs) -> Any: ...
    @classmethod
    def from_orm(self, *args, **kwargs) -> Any: ...
    def json(self, *args, **kwargs) -> Any: ...
    @classmethod
    def parse_file(self, *args, **kwargs) -> Any: ...
    @classmethod
    def parse_obj(self, *args, **kwargs) -> Any: ...
    @classmethod
    def parse_raw(self, *args, **kwargs) -> Any: ...
    @classmethod
    def schema(self, *args, **kwargs) -> Any: ...
    @classmethod
    def schema_json(self, *args, **kwargs) -> Any: ...
    @classmethod
    def update_forward_refs(self, *args, **kwargs) -> Any: ...
    @classmethod
    def validate(self, *args, **kwargs) -> Any: ...
    def __eq__(self, other) -> Any: ...
    @classmethod
    def __get_validators__(self, *args, **kwargs) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __iter__(self) -> Any: ...
    def __json_encoder__(self, *args, **kwargs) -> Any: ...
    def __repr_args__(self, *args, **kwargs) -> Any: ...
    def __setattr__(self, name, value) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    def __signature__(self, *args, **kwargs) -> Any: ...

class NamedTuple:
    _root: ClassVar[bool] = ...
    def __init__(self, *args, **kwargs) -> None: ...
