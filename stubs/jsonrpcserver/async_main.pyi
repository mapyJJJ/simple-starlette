from .async_dispatcher import dispatch_to_response_pure as dispatch_to_response_pure
from .dispatcher import Deserialized as Deserialized
from .main import default_deserializer as default_deserializer, default_validator as default_validator
from .methods import Methods as Methods, global_methods as global_methods
from .response import Response as Response, to_serializable as to_serializable
from .sentinels import NOCONTEXT as NOCONTEXT
from .utils import identity as identity
from typing import Any, Callable, Dict, Iterable, List, Optional, Union

async def dispatch_to_response(request: str, methods: Optional[Methods]=..., *, context: Any=..., deserializer: Callable[[str], Deserialized]=..., validator: Callable[[Deserialized], Deserialized]=..., post_process: Callable[[Response], Any]=...) -> Union[Response, Iterable[Response], None]: ...
async def dispatch_to_serializable(*args: Any, **kwargs: Any) -> Union[Dict[str, Any], List[Dict[str, Any]], None]: ...
async def dispatch_to_json(*args: Any, serializer: Callable[[Union[Dict[str, Any], List[Dict[str, Any]], None]], str]=..., **kwargs: Any) -> str: ...
dispatch = dispatch_to_json
