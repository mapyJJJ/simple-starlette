from ... import util as util
from mypy.nodes import ClassDef as ClassDef, Expression as Expression, MemberExpr, NameExpr, SymbolNode as SymbolNode, TypeInfo
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.types import UnboundType as UnboundType
from typing import List, Optional, Union

COLUMN: int
RELATIONSHIP: int
REGISTRY: int
COLUMN_PROPERTY: int
TYPEENGINE: int
MAPPED: int
DECLARATIVE_BASE: int
DECLARATIVE_META: int
MAPPED_DECORATOR: int
SYNONYM_PROPERTY: int
COMPOSITE_PROPERTY: int
DECLARED_ATTR: int
MAPPER_PROPERTY: int
AS_DECLARATIVE: int
AS_DECLARATIVE_BASE: int
DECLARATIVE_MIXIN: int
QUERY_EXPRESSION: int

def has_base_type_id(info: TypeInfo, type_id: int) -> bool: ...
def mro_has_id(mro: List[TypeInfo], type_id: int) -> bool: ...
def type_id_for_unbound_type(type_: UnboundType, cls: ClassDef, api: SemanticAnalyzerPluginInterface) -> Optional[int]: ...
def type_id_for_callee(callee: Expression) -> Optional[int]: ...
def type_id_for_named_node(node: Union[NameExpr, MemberExpr, SymbolNode]) -> Optional[int]: ...
def type_id_for_fullname(fullname: str) -> Optional[int]: ...
