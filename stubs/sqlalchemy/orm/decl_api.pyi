from . import attributes as attributes, clsregistry as clsregistry, instrumentation as instrumentation, interfaces as interfaces
from .. import exc as exc, inspection as inspection, util as util
from ..sql.schema import MetaData as MetaData
from ..util import hybridmethod as hybridmethod, hybridproperty as hybridproperty
from typing import Any, Optional

def has_inherited_table(cls): ...

class DeclarativeMeta(type):
    def __init__(cls, classname: Any, bases: Any, dict_: Any, **kw: Any) -> None: ...
    def __setattr__(cls, key: Any, value: Any) -> None: ...
    def __delattr__(cls, key: Any) -> None: ...

def synonym_for(name: Any, map_column: bool = ...): ...

class declared_attr(interfaces._MappedAttribute, property):
    __doc__: Any = ...
    def __init__(self, fget: Any, cascading: bool = ...) -> None: ...
    def __get__(desc: Any, self: Any, cls: Any): ...
    def cascading(cls): ...

class _stateful_declared_attr(declared_attr):
    kw: Any = ...
    def __init__(self, **kw: Any) -> None: ...
    def __call__(self, fn: Any): ...

def declarative_mixin(cls): ...
def declarative_base(bind: Optional[Any] = ..., metadata: Optional[Any] = ..., mapper: Optional[Any] = ..., cls: Any = ..., name: str = ..., constructor: Any = ..., class_registry: Optional[Any] = ..., metaclass: Any = ...): ...

class registry:
    metadata: Any = ...
    constructor: Any = ...
    def __init__(self, metadata: Optional[Any] = ..., class_registry: Optional[Any] = ..., constructor: Any = ..., _bind: Optional[Any] = ...) -> None: ...
    @property
    def mappers(self): ...
    def configure(self, cascade: bool = ...) -> None: ...
    def dispose(self, cascade: bool = ...) -> None: ...
    def generate_base(self, mapper: Optional[Any] = ..., cls: Any = ..., name: str = ..., metaclass: Any = ...): ...
    def mapped(self, cls: Any): ...
    def as_declarative_base(self, **kw: Any): ...
    def map_declaratively(self, cls: Any): ...
    def map_imperatively(self, class_: Any, local_table: Optional[Any] = ..., **kw: Any): ...

def as_declarative(**kw: Any): ...
