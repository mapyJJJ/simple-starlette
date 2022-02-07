from ... import util as util
from ...sql import coercions as coercions, elements as elements, expression as expression, functions as functions, roles as roles, schema as schema
from ...sql.schema import ColumnCollectionConstraint as ColumnCollectionConstraint
from .array import ARRAY as ARRAY
from typing import Any, Optional

class aggregate_order_by(expression.ColumnElement):
    __visit_name__: str = ...
    stringify_dialect: str = ...
    target: Any = ...
    type: Any = ...
    order_by: Any = ...
    def __init__(self, target: Any, *order_by: Any) -> None: ...
    def self_group(self, against: Optional[Any] = ...): ...
    def get_children(self, **kwargs: Any): ...

class ExcludeConstraint(ColumnCollectionConstraint):
    __visit_name__: str = ...
    where: Any = ...
    create_drop_stringify_dialect: str = ...
    operators: Any = ...
    using: Any = ...
    ops: Any = ...
    def __init__(self, *elements: Any, **kw: Any) -> None: ...

def array_agg(*arg: Any, **kw: Any): ...