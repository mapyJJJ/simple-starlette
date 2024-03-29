"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

class HasDescriptionCode:
    code: Any = ...
    def __init__(self, *arg: Any, **kw: Any) -> None:
        ...
    


class SQLAlchemyError(HasDescriptionCode, Exception):
    def __unicode__(self):
        ...
    


class ArgumentError(SQLAlchemyError):
    ...


class ObjectNotExecutableError(ArgumentError):
    target: Any = ...
    def __init__(self, target: Any) -> None:
        ...
    
    def __reduce__(self):
        ...
    


class NoSuchModuleError(ArgumentError):
    ...


class NoForeignKeysError(ArgumentError):
    ...


class AmbiguousForeignKeysError(ArgumentError):
    ...


class CircularDependencyError(SQLAlchemyError):
    cycles: Any = ...
    edges: Any = ...
    def __init__(self, message: Any, cycles: Any, edges: Any, msg: Optional[Any] = ..., code: Optional[Any] = ...) -> None:
        ...
    
    def __reduce__(self):
        ...
    


class CompileError(SQLAlchemyError):
    ...


class UnsupportedCompilationError(CompileError):
    code: str = ...
    compiler: Any = ...
    element_type: Any = ...
    message: Any = ...
    def __init__(self, compiler: Any, element_type: Any, message: Optional[Any] = ...) -> None:
        ...
    
    def __reduce__(self):
        ...
    


class IdentifierError(SQLAlchemyError):
    ...


class DisconnectionError(SQLAlchemyError):
    invalidate_pool: bool = ...


class InvalidatePoolError(DisconnectionError):
    invalidate_pool: bool = ...


class TimeoutError(SQLAlchemyError):
    ...


class InvalidRequestError(SQLAlchemyError):
    ...


class NoInspectionAvailable(InvalidRequestError):
    ...


class PendingRollbackError(InvalidRequestError):
    ...


class ResourceClosedError(InvalidRequestError):
    ...


class NoSuchColumnError(InvalidRequestError, KeyError):
    ...


class NoResultFound(InvalidRequestError):
    ...


class MultipleResultsFound(InvalidRequestError):
    ...


class NoReferenceError(InvalidRequestError):
    ...


class AwaitRequired(InvalidRequestError):
    code: str = ...


class MissingGreenlet(InvalidRequestError):
    code: str = ...


class NoReferencedTableError(NoReferenceError):
    table_name: Any = ...
    def __init__(self, message: Any, tname: Any) -> None:
        ...
    
    def __reduce__(self):
        ...
    


class NoReferencedColumnError(NoReferenceError):
    table_name: Any = ...
    column_name: Any = ...
    def __init__(self, message: Any, tname: Any, cname: Any) -> None:
        ...
    
    def __reduce__(self):
        ...
    


class NoSuchTableError(InvalidRequestError):
    ...


class UnreflectableTableError(InvalidRequestError):
    ...


class UnboundExecutionError(InvalidRequestError):
    ...


class DontWrapMixin:
    ...


class StatementError(SQLAlchemyError):
    statement: Any = ...
    params: Any = ...
    orig: Any = ...
    ismulti: Any = ...
    hide_parameters: Any = ...
    detail: Any = ...
    def __init__(self, message: Any, statement: Any, params: Any, orig: Any, hide_parameters: bool = ..., code: Optional[Any] = ..., ismulti: Optional[Any] = ...) -> None:
        ...
    
    def add_detail(self, msg: Any) -> None:
        ...
    
    def __reduce__(self):
        ...
    


class DBAPIError(StatementError):
    code: str = ...
    @classmethod
    def instance(cls, statement: Any, params: Any, orig: Any, dbapi_base_err: Any, hide_parameters: bool = ..., connection_invalidated: bool = ..., dialect: Optional[Any] = ..., ismulti: Optional[Any] = ...):
        ...
    
    def __reduce__(self):
        ...
    
    connection_invalidated: Any = ...
    def __init__(self, statement: Any, params: Any, orig: Any, hide_parameters: bool = ..., connection_invalidated: bool = ..., code: Optional[Any] = ..., ismulti: Optional[Any] = ...) -> None:
        ...
    


class InterfaceError(DBAPIError):
    code: str = ...


class DatabaseError(DBAPIError):
    code: str = ...


class DataError(DatabaseError):
    code: str = ...


class OperationalError(DatabaseError):
    code: str = ...


class IntegrityError(DatabaseError):
    code: str = ...


class InternalError(DatabaseError):
    code: str = ...


class ProgrammingError(DatabaseError):
    code: str = ...


class NotSupportedError(DatabaseError):
    code: str = ...


class SADeprecationWarning(HasDescriptionCode, DeprecationWarning):
    deprecated_since: Any = ...


class Base20DeprecationWarning(SADeprecationWarning):
    deprecated_since: str = ...


class LegacyAPIWarning(Base20DeprecationWarning):
    ...


class RemovedIn20Warning(Base20DeprecationWarning):
    ...


class MovedIn20Warning(RemovedIn20Warning):
    ...


class SAPendingDeprecationWarning(PendingDeprecationWarning):
    deprecated_since: Any = ...


class SAWarning(HasDescriptionCode, RuntimeWarning):
    ...


