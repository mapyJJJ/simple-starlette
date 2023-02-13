"""
This type stub file was generated by pyright.
"""

from .. import util
from ..sql import operators, roles
from ..sql.base import ExecutableOption
from ..sql.traversals import HasCacheKey
from .base import InspectionAttr, _MappedAttribute
from typing import Any, Optional

class ORMStatementRole(roles.StatementRole):
    ...


class ORMColumnsClauseRole(roles.ColumnsClauseRole):
    ...


class ORMEntityColumnsClauseRole(ORMColumnsClauseRole):
    ...


class ORMFromClauseRole(roles.StrictFromClauseRole):
    ...


class MapperProperty(HasCacheKey, _MappedAttribute, InspectionAttr, util.MemoizedSlots):
    cascade: Any = ...
    is_property: bool = ...
    def setup(self, context: Any, query_entity: Any, path: Any, adapter: Any, **kwargs: Any) -> None:
        ...
    
    def create_row_processor(self, context: Any, query_entity: Any, path: Any, mapper: Any, result: Any, adapter: Any, populators: Any) -> None:
        ...
    
    def cascade_iterator(self, type_: Any, state: Any, dict_: Any, visited_states: Any, halt_on: Optional[Any] = ...):
        ...
    
    parent: Any = ...
    def set_parent(self, parent: Any, init: Any) -> None:
        ...
    
    def instrument_class(self, mapper: Any) -> None:
        ...
    
    def __init__(self) -> None:
        ...
    
    def init(self) -> None:
        ...
    
    @property
    def class_attribute(self):
        ...
    
    def do_init(self) -> None:
        ...
    
    def post_instrument_class(self, mapper: Any) -> None:
        ...
    
    def merge(self, session: Any, source_state: Any, source_dict: Any, dest_state: Any, dest_dict: Any, load: Any, _recursive: Any, _resolve_conflict_map: Any) -> None:
        ...
    


class PropComparator(operators.ColumnOperators):
    __visit_name__: str = ...
    prop: Any = ...
    def __init__(self, prop: Any, parentmapper: Any, adapt_to_entity: Optional[Any] = ...) -> None:
        ...
    
    def __clause_element__(self) -> None:
        ...
    
    def adapt_to_entity(self, adapt_to_entity: Any):
        ...
    
    @property
    def adapter(self):
        ...
    
    @property
    def info(self):
        ...
    
    @staticmethod
    def any_op(a: Any, b: Any, **kwargs: Any):
        ...
    
    @staticmethod
    def has_op(a: Any, b: Any, **kwargs: Any):
        ...
    
    @staticmethod
    def of_type_op(a: Any, class_: Any):
        ...
    
    def of_type(self, class_: Any):
        ...
    
    def and_(self, *criteria: Any):
        ...
    
    def any(self, criterion: Optional[Any] = ..., **kwargs: Any):
        ...
    
    def has(self, criterion: Optional[Any] = ..., **kwargs: Any):
        ...
    


class StrategizedProperty(MapperProperty):
    inherit_cache: bool = ...
    strategy_wildcard_key: Any = ...
    def setup(self, context: Any, query_entity: Any, path: Any, adapter: Any, **kwargs: Any) -> None:
        ...
    
    def create_row_processor(self, context: Any, query_entity: Any, path: Any, mapper: Any, result: Any, adapter: Any, populators: Any) -> None:
        ...
    
    strategy: Any = ...
    def do_init(self) -> None:
        ...
    
    def post_instrument_class(self, mapper: Any) -> None:
        ...
    
    @classmethod
    def strategy_for(cls, **kw: Any):
        ...
    


class ORMOption(ExecutableOption):
    propagate_to_loaders: bool = ...


class LoaderOption(ORMOption):
    def process_compile_state_replaced_entities(self, compile_state: Any, mapper_entities: Any) -> None:
        ...
    
    def process_compile_state(self, compile_state: Any) -> None:
        ...
    


class CriteriaOption(ORMOption):
    def process_compile_state(self, compile_state: Any) -> None:
        ...
    
    def get_global_criteria(self, attributes: Any) -> None:
        ...
    


class UserDefinedOption(ORMOption):
    propagate_to_loaders: bool = ...
    payload: Any = ...
    def __init__(self, payload: Optional[Any] = ...) -> None:
        ...
    


class MapperOption(ORMOption):
    propagate_to_loaders: bool = ...
    def process_query(self, query: Any) -> None:
        ...
    
    def process_query_conditionally(self, query: Any) -> None:
        ...
    


class LoaderStrategy:
    parent_property: Any = ...
    is_class_level: bool = ...
    parent: Any = ...
    key: Any = ...
    strategy_key: Any = ...
    strategy_opts: Any = ...
    def __init__(self, parent: Any, strategy_key: Any) -> None:
        ...
    
    def init_class_attribute(self, mapper: Any) -> None:
        ...
    
    def setup_query(self, compile_state: Any, query_entity: Any, path: Any, loadopt: Any, adapter: Any, **kwargs: Any) -> None:
        ...
    
    def create_row_processor(self, context: Any, query_entity: Any, path: Any, loadopt: Any, mapper: Any, result: Any, adapter: Any, populators: Any) -> None:
        ...
    


