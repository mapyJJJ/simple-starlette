from typing import Any, Callable, List

identity: Any

def compose(*fs: Callable[..., Any]) -> Callable[..., Any]: ...
def make_list(x: Any) -> List[Any]: ...
