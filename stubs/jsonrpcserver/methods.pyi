from .result import Result as Result
from typing import Any, Callable, Dict, Optional

Method = Callable[..., Result]
Methods = Dict[str, Method]
global_methods: Any

def method(f: Optional[Method]=..., name: Optional[str]=...) -> Callable[..., Any]: ...
