"""
This type stub file was generated by pyright.
"""

from ... import types as sqltypes
from typing import Any

class RangeOperators:
    class comparator_factory(sqltypes.Concatenable.Comparator):
        def __ne__(self, other: Any) -> Any:
            ...
        
        def contains(self, other: Any, **kw: Any):
            ...
        
        def contained_by(self, other: Any):
            ...
        
        def overlaps(self, other: Any):
            ...
        
        def strictly_left_of(self, other: Any):
            ...
        
        __lshift__: Any = ...
        def strictly_right_of(self, other: Any):
            ...
        
        __rshift__: Any = ...
        def not_extend_right_of(self, other: Any):
            ...
        
        def not_extend_left_of(self, other: Any):
            ...
        
        def adjacent_to(self, other: Any):
            ...
        
        def __add__(self, other: Any):
            ...
        
    
    


class INT4RANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str = ...


class INT8RANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str = ...


class NUMRANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str = ...


class DATERANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str = ...


class TSRANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str = ...


class TSTZRANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str = ...


