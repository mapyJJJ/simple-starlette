from .codes import ERROR_INVALID_REQUEST as ERROR_INVALID_REQUEST, ERROR_METHOD_NOT_FOUND as ERROR_METHOD_NOT_FOUND, ERROR_PARSE_ERROR as ERROR_PARSE_ERROR, ERROR_SERVER_ERROR as ERROR_SERVER_ERROR
from .sentinels import NODATA as NODATA
from oslash.either import Either
from typing import Any, Dict, List, NamedTuple, Type, Union

Deserialized = Union[Dict[str, Any], List[Dict[str, Any]]]

class SuccessResponse(NamedTuple):
    result: str
    id: Any

class ErrorResponse(NamedTuple):
    code: int
    message: str
    data: Any
    id: Any
Response = Either[ErrorResponse, SuccessResponse]
ResponseType = Type[Either[ErrorResponse, SuccessResponse]]

def ParseErrorResponse(data: Any) -> ErrorResponse: ...
def InvalidRequestResponse(data: Any) -> ErrorResponse: ...
def MethodNotFoundResponse(data: Any, id: Any) -> ErrorResponse: ...
def ServerErrorResponse(data: Any, id: Any) -> ErrorResponse: ...
def serialize_error(response: ErrorResponse) -> Dict[str, Any]: ...
def serialize_success(response: SuccessResponse) -> Dict[str, Any]: ...
def to_serializable_one(response: ResponseType) -> Union[Deserialized, None]: ...
def to_serializable(response: ResponseType) -> Union[Deserialized, None]: ...
