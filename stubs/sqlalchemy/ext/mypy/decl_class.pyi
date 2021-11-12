from . import apply as apply, infer as infer, names as names, util as util
from mypy.nodes import ClassDef as ClassDef, SymbolTableNode as SymbolTableNode
from mypy.plugin import SemanticAnalyzerPluginInterface as SemanticAnalyzerPluginInterface
from mypy.types import ProperType as ProperType, Type as Type
from typing import List, Optional

def scan_declarative_assignments_and_apply_types(cls, api: SemanticAnalyzerPluginInterface, is_mixin_scan: bool=...) -> Optional[List[util.SQLAlchemyAttribute]]: ...
