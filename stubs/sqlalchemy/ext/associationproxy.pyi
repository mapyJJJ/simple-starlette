from .. import exc as exc, inspect as inspect, orm as orm, util as util
from ..orm import collections as collections, interfaces as interfaces
from ..sql import or_ as or_
from ..sql.operators import ColumnOperators as ColumnOperators
from typing import Any, Optional

def association_proxy(target_collection: Any, attr: Any, **kw: Any): ...

ASSOCIATION_PROXY: Any

class AssociationProxy(interfaces.InspectionAttrInfo):
    is_attribute: bool = ...
    extension_type: Any = ...
    target_collection: Any = ...
    value_attr: Any = ...
    creator: Any = ...
    getset_factory: Any = ...
    proxy_factory: Any = ...
    proxy_bulk_set: Any = ...
    cascade_scalar_deletes: Any = ...
    key: Any = ...
    info: Any = ...
    def __init__(self, target_collection: Any, attr: Any, creator: Optional[Any] = ..., getset_factory: Optional[Any] = ..., proxy_factory: Optional[Any] = ..., proxy_bulk_set: Optional[Any] = ..., info: Optional[Any] = ..., cascade_scalar_deletes: bool = ...) -> None: ...
    def __get__(self, obj: Any, class_: Any): ...
    def __set__(self, obj: Any, values: Any): ...
    def __delete__(self, obj: Any): ...
    def for_class(self, class_: Any, obj: Optional[Any] = ...): ...

class AssociationProxyInstance:
    parent: Any = ...
    key: Any = ...
    owning_class: Any = ...
    target_collection: Any = ...
    collection_class: Any = ...
    target_class: Any = ...
    value_attr: Any = ...
    def __init__(self, parent: Any, owning_class: Any, target_class: Any, value_attr: Any) -> None: ...
    @classmethod
    def for_proxy(cls, parent: Any, owning_class: Any, parent_instance: Any): ...
    def __clause_element__(self) -> None: ...
    @property
    def remote_attr(self): ...
    @property
    def local_attr(self): ...
    @property
    def attr(self): ...
    def scalar(self): ...
    @property
    def info(self): ...
    def get(self, obj: Any): ...
    def set(self, obj: Any, values: Any) -> None: ...
    def delete(self, obj: Any) -> None: ...
    def any(self, criterion: Optional[Any] = ..., **kwargs: Any): ...
    def has(self, criterion: Optional[Any] = ..., **kwargs: Any): ...

class AmbiguousAssociationProxyInstance(AssociationProxyInstance):
    def get(self, obj: Any): ...
    def __eq__(self, obj: Any) -> Any: ...
    def __ne__(self, obj: Any) -> Any: ...
    def any(self, criterion: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def has(self, criterion: Optional[Any] = ..., **kwargs: Any) -> None: ...

class ObjectAssociationProxyInstance(AssociationProxyInstance):
    def contains(self, obj: Any): ...
    def __eq__(self, obj: Any) -> Any: ...
    def __ne__(self, obj: Any) -> Any: ...

class ColumnAssociationProxyInstance(ColumnOperators, AssociationProxyInstance):
    def __eq__(self, other: Any) -> Any: ...
    def operate(self, op: Any, *other: Any, **kwargs: Any): ...

class _lazy_collection:
    parent: Any = ...
    target: Any = ...
    def __init__(self, obj: Any, target: Any) -> None: ...
    def __call__(self): ...

class _AssociationCollection:
    lazy_collection: Any = ...
    creator: Any = ...
    getter: Any = ...
    setter: Any = ...
    parent: Any = ...
    def __init__(self, lazy_collection: Any, creator: Any, getter: Any, setter: Any, parent: Any) -> None: ...
    col: Any = ...
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...

class _AssociationList(_AssociationCollection):
    def __getitem__(self, index: Any): ...
    def __setitem__(self, index: Any, value: Any) -> None: ...
    def __delitem__(self, index: Any) -> None: ...
    def __contains__(self, value: Any): ...
    def __getslice__(self, start: Any, end: Any): ...
    def __setslice__(self, start: Any, end: Any, values: Any) -> None: ...
    def __delslice__(self, start: Any, end: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def append(self, value: Any) -> None: ...
    def count(self, value: Any): ...
    def extend(self, values: Any) -> None: ...
    def insert(self, index: Any, value: Any) -> None: ...
    def pop(self, index: int = ...): ...
    def remove(self, value: Any) -> None: ...
    def reverse(self) -> None: ...
    def sort(self) -> None: ...
    def clear(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __cmp__(self, other: Any): ...
    def __add__(self, iterable: Any): ...
    def __radd__(self, iterable: Any): ...
    def __mul__(self, n: Any): ...
    __rmul__: Any = ...
    def __iadd__(self, iterable: Any): ...
    def __imul__(self, n: Any): ...
    def index(self, item: Any, *args: Any): ...
    def copy(self): ...
    def __hash__(self) -> Any: ...

class _AssociationDict(_AssociationCollection):
    def __getitem__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __contains__(self, key: Any): ...
    def has_key(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def clear(self) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __cmp__(self, other: Any): ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def setdefault(self, key: Any, default: Optional[Any] = ...): ...
    def keys(self): ...
    def iteritems(self): ...
    def itervalues(self): ...
    def iterkeys(self): ...
    def values(self): ...
    def items(self): ...
    def items(self): ...
    def values(self): ...
    def pop(self, key: Any, default: Any = ...): ...
    def popitem(self): ...
    def update(self, *a: Any, **kw: Any) -> None: ...
    def copy(self): ...
    def __hash__(self) -> Any: ...

class _AssociationSet(_AssociationCollection):
    def __len__(self): ...
    def __bool__(self): ...
    __nonzero__: Any = ...
    def __contains__(self, value: Any): ...
    def __iter__(self) -> Any: ...
    def add(self, value: Any) -> None: ...
    def discard(self, value: Any) -> None: ...
    def remove(self, value: Any) -> None: ...
    def pop(self): ...
    def update(self, other: Any) -> None: ...
    def __ior__(self, other: Any): ...
    def union(self, other: Any): ...
    __or__: Any = ...
    def difference(self, other: Any): ...
    __sub__: Any = ...
    def difference_update(self, other: Any) -> None: ...
    def __isub__(self, other: Any): ...
    def intersection(self, other: Any): ...
    __and__: Any = ...
    def intersection_update(self, other: Any) -> None: ...
    def __iand__(self, other: Any): ...
    def symmetric_difference(self, other: Any): ...
    __xor__: Any = ...
    def symmetric_difference_update(self, other: Any) -> None: ...
    def __ixor__(self, other: Any): ...
    def issubset(self, other: Any): ...
    def issuperset(self, other: Any): ...
    def clear(self) -> None: ...
    def copy(self): ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
