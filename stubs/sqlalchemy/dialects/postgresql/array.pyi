"""
This type stub file was generated by pyright.
"""

from ... import types as sqltypes
from ...sql import expression as expression
from typing import Any as _Any, Optional

def Any(other: _Any, arrexpr: _Any, operator: _Any = ...):
    ...

def All(other: _Any, arrexpr: _Any, operator: _Any = ...):
    ...

class array(expression.ClauseList, expression.ColumnElement):
    __visit_name__: str = ...
    stringify_dialect: str = ...
    type: _Any = ...
    def __init__(self, clauses: _Any, **kw: _Any) -> None:
        ...
    
    def self_group(self, against: Optional[_Any] = ...):
        ...
    


CONTAINS: _Any
CONTAINED_BY: _Any
OVERLAP: _Any
class ARRAY(sqltypes.ARRAY):
    class Comparator(sqltypes.ARRAY.Comparator):
        def contains(self, other: _Any, **kwargs: _Any):
            ...
        
        def contained_by(self, other: _Any):
            ...
        
        def overlap(self, other: _Any):
            ...
        
    
    
    comparator_factory: _Any = ...
    item_type: _Any = ...
    as_tuple: _Any = ...
    dimensions: _Any = ...
    zero_indexes: _Any = ...
    def __init__(self, item_type: _Any, as_tuple: bool = ..., dimensions: Optional[_Any] = ..., zero_indexes: bool = ...) -> None:
        ...
    
    @property
    def hashable(self):
        ...
    
    @property
    def python_type(self):
        ...
    
    def compare_values(self, x: _Any, y: _Any):
        ...
    
    def bind_expression(self, bindvalue: _Any):
        ...
    
    def bind_processor(self, dialect: _Any):
        ...
    
    def result_processor(self, dialect: _Any, coltype: _Any):
        ...
    


