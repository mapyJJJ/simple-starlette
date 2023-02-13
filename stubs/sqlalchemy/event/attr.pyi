"""
This type stub file was generated by pyright.
"""

from .. import util as util
from typing import Any

class RefCollection(util.MemoizedSlots):
    ...


class _empty_collection:
    def append(self, element: Any) -> None:
        ...
    
    def extend(self, other: Any) -> None:
        ...
    
    def remove(self, element: Any) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def clear(self) -> None:
        ...
    


class _ClsLevelDispatch(RefCollection):
    name: Any = ...
    clsname: Any = ...
    arg_names: Any = ...
    has_kw: Any = ...
    legacy_signatures: Any = ...
    def __init__(self, parent_dispatch_cls: Any, fn: Any) -> None:
        ...
    
    def insert(self, event_key: Any, propagate: Any) -> None:
        ...
    
    def append(self, event_key: Any, propagate: Any) -> None:
        ...
    
    def update_subclass(self, target: Any) -> None:
        ...
    
    def remove(self, event_key: Any) -> None:
        ...
    
    def clear(self) -> None:
        ...
    
    def for_modify(self, obj: Any):
        ...
    


class _InstanceLevelDispatch(RefCollection):
    ...


class _EmptyListener(_InstanceLevelDispatch):
    propagate: Any = ...
    listeners: Any = ...
    parent: Any = ...
    parent_listeners: Any = ...
    name: Any = ...
    def __init__(self, parent: Any, target_cls: Any) -> None:
        ...
    
    def for_modify(self, obj: Any):
        ...
    
    exec_once: Any = ...
    exec_once_unless_exception: Any = ...
    insert: Any = ...
    append: Any = ...
    remove: Any = ...
    clear: Any = ...
    def __call__(self, *args: Any, **kw: Any) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def __bool__(self):
        ...
    
    __nonzero__: Any = ...


class _CompoundListener(_InstanceLevelDispatch):
    def exec_once(self, *args: Any, **kw: Any) -> None:
        ...
    
    def exec_once_unless_exception(self, *args: Any, **kw: Any) -> None:
        ...
    
    def __call__(self, *args: Any, **kw: Any) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def __bool__(self):
        ...
    
    __nonzero__: Any = ...


class _ListenerCollection(_CompoundListener):
    parent_listeners: Any = ...
    parent: Any = ...
    name: Any = ...
    listeners: Any = ...
    propagate: Any = ...
    def __init__(self, parent: Any, target_cls: Any) -> None:
        ...
    
    def for_modify(self, obj: Any):
        ...
    
    def insert(self, event_key: Any, propagate: Any) -> None:
        ...
    
    def append(self, event_key: Any, propagate: Any) -> None:
        ...
    
    def remove(self, event_key: Any) -> None:
        ...
    
    def clear(self) -> None:
        ...
    


class _JoinedListener(_CompoundListener):
    parent: Any = ...
    name: Any = ...
    local: Any = ...
    parent_listeners: Any = ...
    def __init__(self, parent: Any, name: Any, local: Any) -> None:
        ...
    
    @property
    def listeners(self):
        ...
    
    def for_modify(self, obj: Any):
        ...
    
    def insert(self, event_key: Any, propagate: Any) -> None:
        ...
    
    def append(self, event_key: Any, propagate: Any) -> None:
        ...
    
    def remove(self, event_key: Any) -> None:
        ...
    
    def clear(self) -> None:
        ...
    


