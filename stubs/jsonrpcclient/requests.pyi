from . import id_generators as id_generators
from .sentinels import NOID as NOID
from .utils import compose as compose
from typing import Any, Dict, Iterator, Tuple, Union

def notification_pure(method: str, params: Union[Dict[str, Any], Tuple[Any, ...]]) -> Dict[str, Any]: ...
def notification(method: str, params: Union[Dict[str, Any], Tuple[Any, ...], None]=...) -> Dict[str, Any]: ...

notification_json: Any

def request_pure(id_generator: Iterator[Any], method: str, params: Union[Dict[str, Any], Tuple[Any, ...]], id: Any) -> Dict[str, Any]: ...
def request_impure(id_generator: Iterator[Any], method: str, params: Union[Dict[str, Any], Tuple[Any, ...], None]=..., id: Any=...) -> Dict[str, Any]: ...

request_natural: Any
request_hex: Any
request_random: Any
request_uuid: Any
request = request_natural
request_json: Any
request_json_hex: Any
request_json_random: Any
request_json_uuid: Any
