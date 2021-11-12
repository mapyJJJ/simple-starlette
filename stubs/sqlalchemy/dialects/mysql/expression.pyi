from ... import exc as exc, util as util
from ...sql import coercions as coercions, elements as elements, operators as operators, roles as roles
from ...sql.base import Generative as Generative
from typing import Any

class match(Generative, elements.BinaryExpression):
    __visit_name__: str = ...
    inherit_cache: bool = ...
    def __init__(self, *cols: Any, **kw: Any) -> None: ...
    modifiers: Any = ...
    def in_boolean_mode(self) -> None: ...
    def in_natural_language_mode(self) -> None: ...
    def with_query_expansion(self) -> None: ...
