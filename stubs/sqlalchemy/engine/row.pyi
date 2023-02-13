"""
This type stub file was generated by pyright.
"""

from ..util.compat import collections_abc as collections_abc
from sqlalchemy.cresultproxy import BaseRow as BaseRow
from typing import Any

MD_INDEX: int
def rowproxy_reconstructor(cls, state: Any):
    ...

KEY_INTEGER_ONLY: int
KEY_OBJECTS_ONLY: int
KEY_OBJECTS_BUT_WARN: int
KEY_OBJECTS_NO_WARN: int
class BaseRow:
    def __init__(self, parent: Any, processors: Any, keymap: Any, key_style: Any, data: Any) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def __len__(self):
        ...
    
    def __hash__(self) -> Any:
        ...
    
    __getitem__: Any = ...
    def __getattr__(self, name: Any):
        ...
    


class Row(BaseRow, collections_abc.Sequence):
    count: Any = ...
    index: Any = ...
    def __contains__(self, key: Any):
        ...
    
    __hash__: Any = ...
    def __lt__(self, other: Any) -> Any:
        ...
    
    def __le__(self, other: Any) -> Any:
        ...
    
    def __ge__(self, other: Any) -> Any:
        ...
    
    def __gt__(self, other: Any) -> Any:
        ...
    
    def __eq__(self, other: Any) -> Any:
        ...
    
    def __ne__(self, other: Any) -> Any:
        ...
    
    def keys(self):
        ...
    


class LegacyRow(Row):
    def __contains__(self, key: Any):
        ...
    
    def has_key(self, key: Any):
        ...
    
    def items(self):
        ...
    
    def iterkeys(self):
        ...
    
    def itervalues(self):
        ...
    
    def values(self):
        ...
    


BaseRowProxy = BaseRow
RowProxy = Row
class ROMappingView(collections_abc.KeysView, collections_abc.ValuesView, collections_abc.ItemsView):
    def __init__(self, mapping: Any, items: Any) -> None:
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def __contains__(self, item: Any):
        ...
    
    def __eq__(self, other: Any) -> Any:
        ...
    
    def __ne__(self, other: Any) -> Any:
        ...
    


class RowMapping(BaseRow, collections_abc.Mapping):
    __getitem__: Any = ...
    def __iter__(self) -> Any:
        ...
    
    def __len__(self):
        ...
    
    def __contains__(self, key: Any):
        ...
    
    def items(self):
        ...
    
    def keys(self):
        ...
    
    def values(self):
        ...
    


