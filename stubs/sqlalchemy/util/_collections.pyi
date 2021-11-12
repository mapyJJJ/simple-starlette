from .compat import binary_types as binary_types, collections_abc as collections_abc, itertools_filterfalse as itertools_filterfalse, py2k as py2k, py37 as py37, string_types as string_types, threading as threading
from sqlalchemy.cimmutabledict import immutabledict as immutabledict
from typing import Any, Optional

EMPTY_SET: Any

class ImmutableContainer:
    __delitem__: Any = ...
    __setitem__: Any = ...
    __setattr__: Any = ...

def coerce_to_immutabledict(d: Any): ...

EMPTY_DICT: Any

class FacadeDict(ImmutableContainer, dict):
    clear: Any = ...
    pop: Any = ...
    popitem: Any = ...
    setdefault: Any = ...
    update: Any = ...
    def __new__(cls, *args: Any): ...
    def copy(self) -> None: ...
    def __reduce__(self): ...

class Properties:
    def __init__(self, data: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __dir__(self): ...
    def __add__(self, other: Any): ...
    def __setitem__(self, key: Any, obj: Any) -> None: ...
    def __getitem__(self, key: Any): ...
    def __delitem__(self, key: Any) -> None: ...
    def __setattr__(self, key: Any, obj: Any) -> None: ...
    def __getattr__(self, key: Any): ...
    def __contains__(self, key: Any): ...
    def as_immutable(self): ...
    def update(self, value: Any) -> None: ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def has_key(self, key: Any): ...
    def clear(self) -> None: ...

class OrderedProperties(Properties):
    def __init__(self) -> None: ...

class ImmutableProperties(ImmutableContainer, Properties): ...
OrderedDict = dict
sort_dictionary: Any

class OrderedDict(dict):
    def __reduce__(self): ...
    def __init__(self, ____sequence: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def clear(self) -> None: ...
    def copy(self): ...
    def __copy__(self): ...
    def update(self, ____sequence: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def setdefault(self, key: Any, value: Any): ...
    def __iter__(self) -> Any: ...
    def keys(self): ...
    def values(self): ...
    def items(self): ...
    def itervalues(self): ...
    def iterkeys(self): ...
    def iteritems(self): ...
    def __setitem__(self, key: Any, obj: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def pop(self, key: Any, *default: Any): ...
    def popitem(self): ...

class OrderedSet(set):
    def __init__(self, d: Optional[Any] = ...) -> None: ...
    def add(self, element: Any) -> None: ...
    def remove(self, element: Any) -> None: ...
    def insert(self, pos: Any, element: Any) -> None: ...
    def discard(self, element: Any) -> None: ...
    def clear(self) -> None: ...
    def __getitem__(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def __add__(self, other: Any): ...
    def update(self, iterable: Any): ...
    __ior__: Any = ...
    def union(self, other: Any): ...
    __or__: Any = ...
    def intersection(self, other: Any): ...
    __and__: Any = ...
    def symmetric_difference(self, other: Any): ...
    __xor__: Any = ...
    def difference(self, other: Any): ...
    __sub__: Any = ...
    def intersection_update(self, other: Any): ...
    __iand__: Any = ...
    def symmetric_difference_update(self, other: Any): ...
    __ixor__: Any = ...
    def difference_update(self, other: Any): ...
    __isub__: Any = ...

class IdentitySet:
    def __init__(self, iterable: Optional[Any] = ...) -> None: ...
    def add(self, value: Any) -> None: ...
    def __contains__(self, value: Any): ...
    def remove(self, value: Any) -> None: ...
    def discard(self, value: Any) -> None: ...
    def pop(self): ...
    def clear(self) -> None: ...
    def __cmp__(self, other: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def issubset(self, iterable: Any): ...
    def __le__(self, other: Any) -> Any: ...
    def __lt__(self, other: Any) -> Any: ...
    def issuperset(self, iterable: Any): ...
    def __ge__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def union(self, iterable: Any): ...
    def __or__(self, other: Any): ...
    def update(self, iterable: Any) -> None: ...
    def __ior__(self, other: Any): ...
    def difference(self, iterable: Any): ...
    def __sub__(self, other: Any): ...
    def difference_update(self, iterable: Any) -> None: ...
    def __isub__(self, other: Any): ...
    def intersection(self, iterable: Any): ...
    def __and__(self, other: Any): ...
    def intersection_update(self, iterable: Any) -> None: ...
    def __iand__(self, other: Any): ...
    def symmetric_difference(self, iterable: Any): ...
    def __xor__(self, other: Any): ...
    def symmetric_difference_update(self, iterable: Any) -> None: ...
    def __ixor__(self, other: Any): ...
    def copy(self): ...
    __copy__: Any = ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __hash__(self) -> Any: ...

class WeakSequence:
    def __init__(self, __elements: Any = ...) -> None: ...
    def append(self, item: Any) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, index: Any): ...

class OrderedIdentitySet(IdentitySet):
    def __init__(self, iterable: Optional[Any] = ...) -> None: ...

class PopulateDict(dict):
    creator: Any = ...
    def __init__(self, creator: Any) -> None: ...
    def __missing__(self, key: Any): ...

class WeakPopulateDict(dict):
    creator: Any = ...
    weakself: Any = ...
    def __init__(self, creator_method: Any) -> None: ...
    def __missing__(self, key: Any): ...
column_set = set
column_dict = dict
ordered_column_set = OrderedSet

def unique_list(seq: Any, hashfunc: Optional[Any] = ...): ...

class UniqueAppender:
    data: Any = ...
    def __init__(self, data: Any, via: Optional[Any] = ...) -> None: ...
    def append(self, item: Any) -> None: ...
    def __iter__(self) -> Any: ...

def coerce_generator_arg(arg: Any): ...
def to_list(x: Any, default: Optional[Any] = ...): ...
def has_intersection(set_: Any, iterable: Any): ...
def to_set(x: Any): ...
def to_column_set(x: Any): ...
def update_copy(d: Any, _new: Optional[Any] = ..., **kw: Any): ...
def flatten_iterator(x: Any) -> None: ...

class LRUCache(dict):
    capacity: Any = ...
    threshold: Any = ...
    size_alert: Any = ...
    def __init__(self, capacity: int = ..., threshold: float = ..., size_alert: Optional[Any] = ...) -> None: ...
    def get(self, key: Any, default: Optional[Any] = ...): ...
    def __getitem__(self, key: Any): ...
    def values(self): ...
    def setdefault(self, key: Any, value: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    @property
    def size_threshold(self): ...

class ScopedRegistry:
    createfunc: Any = ...
    scopefunc: Any = ...
    registry: Any = ...
    def __init__(self, createfunc: Any, scopefunc: Any) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj: Any) -> None: ...
    def clear(self) -> None: ...

class ThreadLocalRegistry(ScopedRegistry):
    createfunc: Any = ...
    registry: Any = ...
    def __init__(self, createfunc: Any) -> None: ...
    def __call__(self): ...
    def has(self): ...
    def set(self, obj: Any) -> None: ...
    def clear(self) -> None: ...

def has_dupes(sequence: Any, target: Any): ...
