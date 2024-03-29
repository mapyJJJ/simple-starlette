"""
This type stub file was generated by pyright.
"""

from . import base as orm_base
from ..sql.traversals import HasCacheKey as HasCacheKey
from typing import Any, Optional

log: Any
class PathRegistry(HasCacheKey):
    is_token: bool = ...
    is_root: bool = ...
    def __eq__(self, other: Any) -> Any:
        ...
    
    def __ne__(self, other: Any) -> Any:
        ...
    
    def set(self, attributes: Any, key: Any, value: Any) -> None:
        ...
    
    def setdefault(self, attributes: Any, key: Any, value: Any) -> None:
        ...
    
    def get(self, attributes: Any, key: Any, value: Optional[Any] = ...):
        ...
    
    def __len__(self):
        ...
    
    def __hash__(self) -> Any:
        ...
    
    @property
    def length(self):
        ...
    
    def pairs(self) -> None:
        ...
    
    def contains_mapper(self, mapper: Any):
        ...
    
    def contains(self, attributes: Any, key: Any):
        ...
    
    def __reduce__(self):
        ...
    
    @classmethod
    def serialize_context_dict(cls, dict_: Any, tokens: Any):
        ...
    
    @classmethod
    def deserialize_context_dict(cls, serialized: Any):
        ...
    
    def serialize(self):
        ...
    
    @classmethod
    def deserialize(cls, path: Any):
        ...
    
    @classmethod
    def per_mapper(cls, mapper: Any):
        ...
    
    @classmethod
    def coerce(cls, raw: Any):
        ...
    
    def token(self, token: Any):
        ...
    
    def __add__(self, other: Any):
        ...
    


class RootRegistry(PathRegistry):
    inherit_cache: bool = ...
    path: Any = ...
    natural_path: Any = ...
    has_entity: bool = ...
    is_aliased_class: bool = ...
    is_root: bool = ...
    def __getitem__(self, entity: Any):
        ...
    


class PathToken(orm_base.InspectionAttr, HasCacheKey, str):
    @classmethod
    def intern(cls, strvalue: Any):
        ...
    


class TokenRegistry(PathRegistry):
    inherit_cache: bool = ...
    token: Any = ...
    parent: Any = ...
    path: Any = ...
    natural_path: Any = ...
    def __init__(self, parent: Any, token: Any) -> None:
        ...
    
    has_entity: bool = ...
    is_token: bool = ...
    def generate_for_superclasses(self) -> None:
        ...
    
    def __getitem__(self, entity: Any) -> None:
        ...
    


class PropRegistry(PathRegistry):
    is_unnatural: bool = ...
    inherit_cache: bool = ...
    prop: Any = ...
    parent: Any = ...
    path: Any = ...
    natural_path: Any = ...
    def __init__(self, parent: Any, prop: Any) -> None:
        ...
    
    def has_entity(self):
        ...
    
    def entity(self):
        ...
    
    @property
    def mapper(self):
        ...
    
    @property
    def entity_path(self):
        ...
    
    def __getitem__(self, entity: Any):
        ...
    


class AbstractEntityRegistry(PathRegistry):
    has_entity: bool = ...
    key: Any = ...
    parent: Any = ...
    is_aliased_class: Any = ...
    entity: Any = ...
    path: Any = ...
    natural_path: Any = ...
    def __init__(self, parent: Any, entity: Any) -> None:
        ...
    
    @property
    def entity_path(self):
        ...
    
    @property
    def mapper(self):
        ...
    
    def __bool__(self):
        ...
    
    __nonzero__: Any = ...
    def __getitem__(self, entity: Any):
        ...
    


class SlotsEntityRegistry(AbstractEntityRegistry):
    inherit_cache: bool = ...


class CachingEntityRegistry(AbstractEntityRegistry, dict):
    inherit_cache: bool = ...
    def __getitem__(self, entity: Any):
        ...
    
    def __missing__(self, key: Any):
        ...
    


