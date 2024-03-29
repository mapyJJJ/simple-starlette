"""
This type stub file was generated by pyright.
"""

from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement
from typing import Any

class Insert(StandardInsert):
    stringify_dialect: str = ...
    @property
    def inserted(self):
        ...
    
    def inserted_alias(self):
        ...
    
    def on_duplicate_key_update(self, *args: Any, **kw: Any) -> None:
        ...
    


insert: Any
class OnDuplicateClause(ClauseElement):
    __visit_name__: str = ...
    stringify_dialect: str = ...
    inserted_alias: Any = ...
    update: Any = ...
    def __init__(self, inserted_alias: Any, update: Any) -> None:
        ...
    


