import json
from .dispatcher import Deserialized as Deserialized, dispatch_to_response_pure as dispatch_to_response_pure
from .methods import Methods as Methods, global_methods as global_methods
from .response import Response as Response, to_serializable_one as to_serializable_one
from .sentinels import NOCONTEXT as NOCONTEXT
from .utils import identity as identity
from typing import Any, Callable, Dict, List, Optional, Union

default_deserializer = json.loads
schema: Any
klass: Any
default_validator: Any

def dispatch_to_response(request: str, methods: Optional[Methods]=..., *, context: Any=..., deserializer: Callable[[str], Deserialized]=..., validator: Callable[[Deserialized], Deserialized]=..., post_process: Callable[[Response], Any]=...) -> Union[Response, List[Response], None]: ...
def dispatch_to_serializable(*args: Any, **kwargs: Any) -> Union[Dict[str, Any], List[Dict[str, Any]], None]: ...
def dispatch_to_json(*args: Any, serializer: Callable[[Union[Dict[str, Any], List[Dict[str, Any]], str]], str]=..., **kwargs: Any) -> str: ...
dispatch = dispatch_to_json
