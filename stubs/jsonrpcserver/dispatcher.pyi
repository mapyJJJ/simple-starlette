from .exceptions import JsonRpcError as JsonRpcError
from .methods import Method as Method, Methods as Methods
from .request import Request as Request
from .response import ErrorResponse as ErrorResponse, InvalidRequestResponse as InvalidRequestResponse, ParseErrorResponse as ParseErrorResponse, Response as Response, ServerErrorResponse as ServerErrorResponse, SuccessResponse as SuccessResponse
from .result import ErrorResult as ErrorResult, InternalErrorResult as InternalErrorResult, InvalidParamsResult as InvalidParamsResult, MethodNotFoundResult as MethodNotFoundResult, Result as Result, SuccessResult as SuccessResult
from .sentinels import NOCONTEXT as NOCONTEXT, NOID as NOID
from .utils import compose as compose, make_list as make_list
from oslash.either import Either as Either
from typing import Any, Callable, Dict, Iterable, List, Tuple, Union

Deserialized = Union[Dict[str, Any], List[Dict[str, Any]]]

def extract_list(is_batch: bool, responses: Iterable[Response]) -> Union[Response, List[Response], None]: ...
def to_response(request: Request, result: Result) -> Response: ...
def extract_args(request: Request, context: Any) -> List[Any]: ...
def extract_kwargs(request: Request) -> Dict[str, Any]: ...
def validate_result(result: Result) -> None: ...
def call(request: Request, context: Any, method: Method) -> Result: ...
def validate_args(request: Request, context: Any, func: Method) -> Either[ErrorResult, Method]: ...
def get_method(methods: Methods, method_name: str) -> Either[ErrorResult, Method]: ...
def dispatch_request(methods: Methods, context: Any, request: Request) -> Tuple[Request, Result]: ...
def create_request(request: Dict[str, Any]) -> Request: ...
def not_notification(request_result: Any) -> bool: ...
def dispatch_deserialized(methods: Methods, context: Any, post_process: Callable[[Response], Iterable[Any]], deserialized: Deserialized) -> Union[Response, List[Response], None]: ...
def validate_request(validator: Callable[[Deserialized], Deserialized], request: Deserialized) -> Either[ErrorResponse, Deserialized]: ...
def deserialize_request(deserializer: Callable[[str], Deserialized], request: str) -> Either[ErrorResponse, Deserialized]: ...
def dispatch_to_response_pure(deserializer: Callable[[str], Deserialized], validator: Callable[[Deserialized], Deserialized], methods: Methods, context: Any, post_process: Callable[[Response], Iterable[Any]], request: str) -> Union[Response, List[Response], None]: ...
