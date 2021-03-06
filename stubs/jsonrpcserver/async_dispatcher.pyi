from .dispatcher import Deserialized as Deserialized, create_request as create_request, deserialize_request as deserialize_request, extract_args as extract_args, extract_kwargs as extract_kwargs, extract_list as extract_list, get_method as get_method, not_notification as not_notification, to_response as to_response, validate_args as validate_args, validate_request as validate_request, validate_result as validate_result
from .exceptions import JsonRpcError as JsonRpcError
from .methods import Method as Method, Methods as Methods
from .request import Request as Request
from .response import Response as Response, ServerErrorResponse as ServerErrorResponse
from .result import ErrorResult as ErrorResult, InternalErrorResult as InternalErrorResult, Result as Result
from .utils import make_list as make_list
from typing import Any, Callable, Iterable, Tuple, Union

async def call(request: Request, context: Any, method: Method) -> Result: ...
async def dispatch_request(methods: Methods, context: Any, request: Request) -> Tuple[Request, Result]: ...
async def dispatch_deserialized(methods: Methods, context: Any, post_process: Callable[[Response], Iterable[Any]], deserialized: Deserialized) -> Union[Response, Iterable[Response], None]: ...
async def dispatch_to_response_pure(deserializer: Callable[[str], Deserialized], validator: Callable[[Deserialized], Deserialized], methods: Methods, context: Any, post_process: Callable[[Response], Iterable[Any]], request: str) -> Union[Response, Iterable[Response], None]: ...
