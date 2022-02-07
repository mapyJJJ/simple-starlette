from ... import inspection as inspection, util as util
from ...orm import registry as registry, relationships as relationships
from ...orm.util import polymorphic_union as polymorphic_union
from ...schema import Table as Table
from ...util import OrderedDict as OrderedDict
from typing import Any

def instrument_declarative(cls, cls_registry: Any, metadata: Any) -> None: ...

class ConcreteBase:
    @classmethod
    def __declare_first__(cls) -> None: ...

class AbstractConcreteBase(ConcreteBase):
    __no_table__: bool = ...
    @classmethod
    def __declare_first__(cls) -> None: ...

class DeferredReflection:
    @classmethod
    def prepare(cls, engine: Any) -> None: ...
