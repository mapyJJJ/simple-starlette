from .class_validators import gather_all_validators as gather_all_validators
from .fields import DeferredType as DeferredType
from .main import BaseModel as BaseModel, create_model as create_model
from .typing import display_as_type as display_as_type, get_all_type_hints as get_all_type_hints, get_args as get_args, get_origin as get_origin, typing_base as typing_base
from .utils import all_identical as all_identical, lenient_issubclass as lenient_issubclass
from typing import Any, ClassVar, Iterator, Mapping, Optional, Tuple, Type, TypeVar, Union

GenericModelT = TypeVar('GenericModelT', bound='GenericModel')
TypeVarType = Any

class GenericModel(BaseModel):
    __concrete__: ClassVar[bool] = ...
    __parameters__: ClassVar[Tuple[TypeVarType, ...]]
    def __class_getitem__(cls, params: Union[Type[Any], Tuple[Type[Any], ...]]) -> Type[Any]: ...
    @classmethod
    def __concrete_name__(cls, params: Tuple[Type[Any], ...]) -> str: ...

def replace_types(type_: Any, type_map: Mapping[Any, Any]) -> Any: ...
def check_parameters_count(cls, parameters: Tuple[Any, ...]) -> None: ...

DictValues: Type[Any]

def iter_contained_typevars(v: Any) -> Iterator[TypeVarType]: ...
def get_caller_frame_info() -> Tuple[Optional[str], bool]: ...
