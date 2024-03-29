"""
This type stub file was generated by pyright.
"""

from ... import types as sqltypes
from typing import Any, Optional

class _NumericType:
    unsigned: Any = ...
    zerofill: Any = ...
    def __init__(self, unsigned: bool = ..., zerofill: bool = ..., **kw: Any) -> None:
        ...
    


class _FloatType(_NumericType, sqltypes.Float):
    scale: Any = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw: Any) -> None:
        ...
    


class _IntegerType(_NumericType, sqltypes.Integer):
    display_width: Any = ...
    def __init__(self, display_width: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class _StringType(sqltypes.String):
    charset: Any = ...
    ascii: Any = ...
    unicode: Any = ...
    binary: Any = ...
    national: Any = ...
    def __init__(self, charset: Optional[Any] = ..., collation: Optional[Any] = ..., ascii: bool = ..., binary: bool = ..., unicode: bool = ..., national: bool = ..., **kw: Any) -> None:
        ...
    


class _MatchType(sqltypes.Float, sqltypes.MatchType):
    def __init__(self, **kw: Any) -> None:
        ...
    


class NUMERIC(_NumericType, sqltypes.NUMERIC):
    __visit_name__: str = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw: Any) -> None:
        ...
    


class DECIMAL(_NumericType, sqltypes.DECIMAL):
    __visit_name__: str = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw: Any) -> None:
        ...
    


class DOUBLE(_FloatType):
    __visit_name__: str = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw: Any) -> None:
        ...
    


class REAL(_FloatType, sqltypes.REAL):
    __visit_name__: str = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw: Any) -> None:
        ...
    


class FLOAT(_FloatType, sqltypes.FLOAT):
    __visit_name__: str = ...
    def __init__(self, precision: Optional[Any] = ..., scale: Optional[Any] = ..., asdecimal: bool = ..., **kw: Any) -> None:
        ...
    
    def bind_processor(self, dialect: Any) -> None:
        ...
    


class INTEGER(_IntegerType, sqltypes.INTEGER):
    __visit_name__: str = ...
    def __init__(self, display_width: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class BIGINT(_IntegerType, sqltypes.BIGINT):
    __visit_name__: str = ...
    def __init__(self, display_width: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class MEDIUMINT(_IntegerType):
    __visit_name__: str = ...
    def __init__(self, display_width: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class TINYINT(_IntegerType):
    __visit_name__: str = ...
    def __init__(self, display_width: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class SMALLINT(_IntegerType, sqltypes.SMALLINT):
    __visit_name__: str = ...
    def __init__(self, display_width: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class BIT(sqltypes.TypeEngine):
    __visit_name__: str = ...
    length: Any = ...
    def __init__(self, length: Optional[Any] = ...) -> None:
        ...
    
    def result_processor(self, dialect: Any, coltype: Any):
        ...
    


class TIME(sqltypes.TIME):
    __visit_name__: str = ...
    fsp: Any = ...
    def __init__(self, timezone: bool = ..., fsp: Optional[Any] = ...) -> None:
        ...
    
    def result_processor(self, dialect: Any, coltype: Any):
        ...
    


class TIMESTAMP(sqltypes.TIMESTAMP):
    __visit_name__: str = ...
    fsp: Any = ...
    def __init__(self, timezone: bool = ..., fsp: Optional[Any] = ...) -> None:
        ...
    


class DATETIME(sqltypes.DATETIME):
    __visit_name__: str = ...
    fsp: Any = ...
    def __init__(self, timezone: bool = ..., fsp: Optional[Any] = ...) -> None:
        ...
    


class YEAR(sqltypes.TypeEngine):
    __visit_name__: str = ...
    display_width: Any = ...
    def __init__(self, display_width: Optional[Any] = ...) -> None:
        ...
    


class TEXT(_StringType, sqltypes.TEXT):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kw: Any) -> None:
        ...
    


class TINYTEXT(_StringType):
    __visit_name__: str = ...
    def __init__(self, **kwargs: Any) -> None:
        ...
    


class MEDIUMTEXT(_StringType):
    __visit_name__: str = ...
    def __init__(self, **kwargs: Any) -> None:
        ...
    


class LONGTEXT(_StringType):
    __visit_name__: str = ...
    def __init__(self, **kwargs: Any) -> None:
        ...
    


class VARCHAR(_StringType, sqltypes.VARCHAR):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None:
        ...
    


class CHAR(_StringType, sqltypes.CHAR):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None:
        ...
    


class NVARCHAR(_StringType, sqltypes.NVARCHAR):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None:
        ...
    


class NCHAR(_StringType, sqltypes.NCHAR):
    __visit_name__: str = ...
    def __init__(self, length: Optional[Any] = ..., **kwargs: Any) -> None:
        ...
    


class TINYBLOB(sqltypes._Binary):
    __visit_name__: str = ...


class MEDIUMBLOB(sqltypes._Binary):
    __visit_name__: str = ...


class LONGBLOB(sqltypes._Binary):
    __visit_name__: str = ...


