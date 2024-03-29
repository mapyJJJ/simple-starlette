"""
This type stub file was generated by pyright.
"""

from . import operators as operators, roles as roles
from .. import util as util
from .annotation import Annotated as Annotated, SupportsWrappingAnnotations as SupportsWrappingAnnotations
from .base import Executable as Executable, Immutable as Immutable, SingletonConstant as SingletonConstant
from .traversals import HasCopyInternals as HasCopyInternals, MemoizedHasCacheKey as MemoizedHasCacheKey
from .visitors import Traversible as Traversible
from typing import Any, Optional

def collate(expression: Any, collation: Any):
    ...

def between(expr: Any, lower_bound: Any, upper_bound: Any, symmetric: bool = ...):
    ...

def literal(value: Any, type_: Optional[Any] = ...):
    ...

def outparam(key: Any, type_: Optional[Any] = ...):
    ...

def not_(clause: Any):
    ...

class ClauseElement(roles.SQLRole, SupportsWrappingAnnotations, MemoizedHasCacheKey, HasCopyInternals, Traversible):
    __visit_name__: str = ...
    supports_execution: bool = ...
    stringify_dialect: str = ...
    bind: Any = ...
    description: Any = ...
    is_clause_element: bool = ...
    is_selectable: bool = ...
    @property
    def entity_namespace(self) -> None:
        ...
    
    def unique_params(self, *optionaldict: Any, **kwargs: Any):
        ...
    
    def params(self, *optionaldict: Any, **kwargs: Any):
        ...
    
    def compare(self, other: Any, **kw: Any):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    
    def compile(self, bind: Optional[Any] = ..., dialect: Optional[Any] = ..., **kw: Any):
        ...
    
    def __invert__(self):
        ...
    
    def __bool__(self) -> None:
        ...
    
    __nonzero__: Any = ...


class ColumnElement(roles.ColumnArgumentOrKeyRole, roles.StatementOptionRole, roles.WhereHavingRole, roles.BinaryElementRole, roles.OrderByRole, roles.ColumnsClauseRole, roles.LimitOffsetRole, roles.DMLColumnRole, roles.DDLConstraintColumnRole, roles.DDLExpressionRole, operators.ColumnOperators, ClauseElement):
    __visit_name__: str = ...
    primary_key: bool = ...
    foreign_keys: Any = ...
    key: Any = ...
    def self_group(self, against: Optional[Any] = ...):
        ...
    
    def type(self):
        ...
    
    def comparator(self):
        ...
    
    def __getattr__(self, key: Any):
        ...
    
    def operate(self, op: Any, *other: Any, **kwargs: Any):
        ...
    
    def reverse_operate(self, op: Any, other: Any, **kwargs: Any):
        ...
    
    @property
    def expression(self):
        ...
    
    def base_columns(self):
        ...
    
    def proxy_set(self):
        ...
    
    def shares_lineage(self, othercolumn: Any):
        ...
    
    def cast(self, type_: Any):
        ...
    
    def label(self, name: Any):
        ...
    
    @property
    def anon_label(self):
        ...
    
    @property
    def anon_key_label(self):
        ...
    


class WrapsColumnExpression:
    @property
    def wrapped_column_expression(self) -> None:
        ...
    


class BindParameter(roles.InElementRole, ColumnElement):
    __visit_name__: str = ...
    inherit_cache: bool = ...
    key: Any = ...
    unique: Any = ...
    value: Any = ...
    callable: Any = ...
    isoutparam: Any = ...
    required: Any = ...
    expanding: Any = ...
    expand_op: Any = ...
    literal_execute: Any = ...
    type: Any = ...
    def __init__(self, key: Any, value: Any = ..., type_: Optional[Any] = ..., unique: bool = ..., required: Any = ..., quote: Optional[Any] = ..., callable_: Optional[Any] = ..., expanding: bool = ..., isoutparam: bool = ..., literal_execute: bool = ..., _compared_to_operator: Optional[Any] = ..., _compared_to_type: Optional[Any] = ..., _is_crud: bool = ...) -> None:
        ...
    
    @property
    def effective_value(self):
        ...
    
    def render_literal_execute(self):
        ...
    


class TypeClause(ClauseElement):
    __visit_name__: str = ...
    type: Any = ...
    def __init__(self, type_: Any) -> None:
        ...
    


class TextClause(roles.DDLConstraintColumnRole, roles.DDLExpressionRole, roles.StatementOptionRole, roles.WhereHavingRole, roles.OrderByRole, roles.FromClauseRole, roles.SelectStatementRole, roles.BinaryElementRole, roles.InElementRole, Executable, ClauseElement):
    __visit_name__: str = ...
    def __and__(self, other: Any):
        ...
    
    key: Any = ...
    text: Any = ...
    def __init__(self, text: Any, bind: Optional[Any] = ...) -> None:
        ...
    
    def bindparams(self, *binds: Any, **names_to_values: Any) -> None:
        ...
    
    def columns(self, *cols: Any, **types: Any):
        ...
    
    @property
    def type(self):
        ...
    
    @property
    def comparator(self):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class Null(SingletonConstant, roles.ConstExprRole, ColumnElement):
    __visit_name__: str = ...
    def type(self):
        ...
    


class False_(SingletonConstant, roles.ConstExprRole, ColumnElement):
    __visit_name__: str = ...
    def type(self):
        ...
    


class True_(SingletonConstant, roles.ConstExprRole, ColumnElement):
    __visit_name__: str = ...
    def type(self):
        ...
    


class ClauseList(roles.InElementRole, roles.OrderByRole, roles.ColumnsClauseRole, roles.DMLColumnRole, ClauseElement):
    __visit_name__: str = ...
    operator: Any = ...
    group: Any = ...
    group_contents: Any = ...
    clauses: Any = ...
    def __init__(self, *clauses: Any, **kwargs: Any) -> None:
        ...
    
    def __iter__(self) -> Any:
        ...
    
    def __len__(self):
        ...
    
    def append(self, clause: Any) -> None:
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class BooleanClauseList(ClauseList, ColumnElement):
    __visit_name__: str = ...
    inherit_cache: bool = ...
    def __init__(self, *arg: Any, **kw: Any) -> None:
        ...
    
    @classmethod
    def and_(cls, *clauses: Any):
        ...
    
    @classmethod
    def or_(cls, *clauses: Any):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


and_: Any
or_: Any
class Tuple(ClauseList, ColumnElement):
    __visit_name__: str = ...
    type: Any = ...
    def __init__(self, *clauses: Any, **kw: Any) -> None:
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class Case(ColumnElement):
    __visit_name__: str = ...
    value: Any = ...
    type: Any = ...
    whens: Any = ...
    else_: Any = ...
    def __init__(self, *whens: Any, **kw: Any) -> None:
        ...
    


def literal_column(text: Any, type_: Optional[Any] = ...):
    ...

class Cast(WrapsColumnExpression, ColumnElement):
    __visit_name__: str = ...
    type: Any = ...
    clause: Any = ...
    typeclause: Any = ...
    def __init__(self, expression: Any, type_: Any) -> None:
        ...
    
    @property
    def wrapped_column_expression(self):
        ...
    


class TypeCoerce(WrapsColumnExpression, ColumnElement):
    __visit_name__: str = ...
    type: Any = ...
    clause: Any = ...
    def __init__(self, expression: Any, type_: Any) -> None:
        ...
    
    def typed_expression(self):
        ...
    
    @property
    def wrapped_column_expression(self):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class Extract(ColumnElement):
    __visit_name__: str = ...
    type: Any = ...
    field: Any = ...
    expr: Any = ...
    def __init__(self, field: Any, expr: Any, **kwargs: Any) -> None:
        ...
    


class _label_reference(ColumnElement):
    __visit_name__: str = ...
    element: Any = ...
    def __init__(self, element: Any) -> None:
        ...
    


class _textual_label_reference(ColumnElement):
    __visit_name__: str = ...
    element: Any = ...
    def __init__(self, element: Any) -> None:
        ...
    


class UnaryExpression(ColumnElement):
    __visit_name__: str = ...
    operator: Any = ...
    modifier: Any = ...
    element: Any = ...
    type: Any = ...
    wraps_column_expression: Any = ...
    def __init__(self, element: Any, operator: Optional[Any] = ..., modifier: Optional[Any] = ..., type_: Optional[Any] = ..., wraps_column_expression: bool = ...) -> None:
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class CollectionAggregate(UnaryExpression):
    def operate(self, op: Any, *other: Any, **kwargs: Any):
        ...
    
    def reverse_operate(self, op: Any, other: Any, **kwargs: Any) -> None:
        ...
    


class AsBoolean(WrapsColumnExpression, UnaryExpression):
    inherit_cache: bool = ...
    element: Any = ...
    type: Any = ...
    operator: Any = ...
    negate: Any = ...
    modifier: Any = ...
    wraps_column_expression: bool = ...
    def __init__(self, element: Any, operator: Any, negate: Any) -> None:
        ...
    
    @property
    def wrapped_column_expression(self):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class BinaryExpression(ColumnElement):
    __visit_name__: str = ...
    left: Any = ...
    right: Any = ...
    operator: Any = ...
    type: Any = ...
    negate: Any = ...
    modifiers: Any = ...
    def __init__(self, left: Any, right: Any, operator: Any, type_: Optional[Any] = ..., negate: Optional[Any] = ..., modifiers: Optional[Any] = ...) -> None:
        ...
    
    def __bool__(self):
        ...
    
    __nonzero__: Any = ...
    @property
    def is_comparison(self):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class Slice(ColumnElement):
    __visit_name__: str = ...
    start: Any = ...
    stop: Any = ...
    step: Any = ...
    type: Any = ...
    def __init__(self, start: Any, stop: Any, step: Any, _name: Optional[Any] = ...) -> None:
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class IndexExpression(BinaryExpression):
    ...


class GroupedElement(ClauseElement):
    __visit_name__: str = ...
    def self_group(self, against: Optional[Any] = ...):
        ...
    


class Grouping(GroupedElement, ColumnElement):
    element: Any = ...
    type: Any = ...
    def __init__(self, element: Any) -> None:
        ...
    
    def __getattr__(self, attr: Any):
        ...
    


RANGE_UNBOUNDED: Any
RANGE_CURRENT: Any
class Over(ColumnElement):
    __visit_name__: str = ...
    order_by: Any = ...
    partition_by: Any = ...
    element: Any = ...
    range_: Any = ...
    rows: Any = ...
    def __init__(self, element: Any, partition_by: Optional[Any] = ..., order_by: Optional[Any] = ..., range_: Optional[Any] = ..., rows: Optional[Any] = ...) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def type(self):
        ...
    


class WithinGroup(ColumnElement):
    __visit_name__: str = ...
    order_by: Any = ...
    element: Any = ...
    def __init__(self, element: Any, *order_by: Any) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def over(self, partition_by: Optional[Any] = ..., order_by: Optional[Any] = ..., range_: Optional[Any] = ..., rows: Optional[Any] = ...):
        ...
    
    def type(self):
        ...
    


class FunctionFilter(ColumnElement):
    __visit_name__: str = ...
    criterion: Any = ...
    func: Any = ...
    def __init__(self, func: Any, *criterion: Any) -> None:
        ...
    
    def filter(self, *criterion: Any):
        ...
    
    def over(self, partition_by: Optional[Any] = ..., order_by: Optional[Any] = ..., range_: Optional[Any] = ..., rows: Optional[Any] = ...):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    
    def type(self):
        ...
    


class Label(roles.LabeledColumnExprRole, ColumnElement):
    __visit_name__: str = ...
    name: Any = ...
    key: Any = ...
    def __init__(self, name: Any, element: Any, type_: Optional[Any] = ...) -> None:
        ...
    
    def __reduce__(self):
        ...
    
    def type(self):
        ...
    
    def element(self):
        ...
    
    def self_group(self, against: Optional[Any] = ...):
        ...
    
    @property
    def primary_key(self):
        ...
    
    @property
    def foreign_keys(self):
        ...
    


class NamedColumn(ColumnElement):
    is_literal: bool = ...
    table: Any = ...
    def description(self):
        ...
    


class ColumnClause(roles.DDLReferredColumnRole, roles.LabeledColumnExprRole, roles.StrAsPlainColumnRole, Immutable, NamedColumn):
    table: Any = ...
    is_literal: bool = ...
    __visit_name__: str = ...
    onupdate: Any = ...
    default: Any = ...
    server_default: Any = ...
    server_onupdate: Any = ...
    key: Any = ...
    type: Any = ...
    def __init__(self, text: Any, type_: Optional[Any] = ..., is_literal: bool = ..., _selectable: Optional[Any] = ...) -> None:
        ...
    
    def get_children(self, column_tables: bool = ..., **kw: Any):
        ...
    
    @property
    def entity_namespace(self):
        ...
    


class TableValuedColumn(NamedColumn):
    __visit_name__: str = ...
    scalar_alias: Any = ...
    key: Any = ...
    type: Any = ...
    def __init__(self, scalar_alias: Any, type_: Any) -> None:
        ...
    


class CollationClause(ColumnElement):
    __visit_name__: str = ...
    collation: Any = ...
    def __init__(self, collation: Any) -> None:
        ...
    


class _IdentifiedClause(Executable, ClauseElement):
    __visit_name__: str = ...
    ident: Any = ...
    def __init__(self, ident: Any) -> None:
        ...
    


class SavepointClause(_IdentifiedClause):
    __visit_name__: str = ...


class RollbackToSavepointClause(_IdentifiedClause):
    __visit_name__: str = ...


class ReleaseSavepointClause(_IdentifiedClause):
    __visit_name__: str = ...


class quoted_name(util.MemoizedSlots, util.text_type):
    quote: Any = ...
    def __new__(cls, value: Any, quote: Any):
        ...
    
    def __reduce__(self):
        ...
    


class AnnotatedColumnElement(Annotated):
    def __init__(self, element: Any, values: Any) -> None:
        ...
    
    def name(self):
        ...
    
    def table(self):
        ...
    
    def key(self):
        ...
    
    def info(self):
        ...
    


class _truncated_label(quoted_name):
    def __new__(cls, value: Any, quote: Optional[Any] = ...):
        ...
    
    def __reduce__(self):
        ...
    
    def apply_map(self, map_: Any):
        ...
    


class conv(_truncated_label):
    ...


class _anonymous_label(_truncated_label):
    @classmethod
    def safe_construct(cls, seed: Any, body: Any, enclosing_label: Optional[Any] = ..., sanitize_key: bool = ...):
        ...
    
    def __add__(self, other: Any):
        ...
    
    def __radd__(self, other: Any):
        ...
    
    def apply_map(self, map_: Any):
        ...
    


