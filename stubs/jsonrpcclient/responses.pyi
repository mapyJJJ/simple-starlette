from .utils import compose as compose
from typing import Any, Dict, Iterable, List, NamedTuple, Union

Deserialized = Union[Dict[str, Any], List[Dict[str, Any]]]

class Ok(NamedTuple):
    result: Any
    id: Any

class Error(NamedTuple):
    code: int
    message: str
    data: Any
    id: Any
Response = Union[Ok, Error]

def to_result(response: Dict[str, Any]) -> Response: ...
def parse(response: Deserialized) -> Union[Response, Iterable[Response]]: ...

parse_json: Any
