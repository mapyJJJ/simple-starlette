from .monkey import get_unpatched as get_unpatched
from typing import Any

have_pyrex: Any

class Extension(_Extension):
    py_limited_api: Any = ...
    def __init__(self, name: Any, sources: Any, *args: Any, **kw: Any) -> None: ...

class Library(Extension): ...
