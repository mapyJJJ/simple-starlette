import code
import typing as t
from ..local import Local as Local
from .repr import debug_repr as debug_repr, dump as dump, helper as helper
from types import CodeType
from typing import Any

class HTMLStringO:
    def __init__(self) -> None: ...
    def isatty(self) -> bool: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    def seek(self, n: int, mode: int=...) -> None: ...
    def readline(self) -> str: ...
    def reset(self) -> str: ...
    def write(self, x: str) -> None: ...
    def writelines(self, x: t.Iterable[str]) -> None: ...

class ThreadedStream:
    @staticmethod
    def push() -> None: ...
    @staticmethod
    def fetch() -> str: ...
    @staticmethod
    def displayhook(obj: object) -> None: ...
    def __setattr__(self, name: str, value: t.Any) -> None: ...
    def __dir__(self) -> t.List[str]: ...
    def __getattribute__(self, name: str) -> t.Any: ...

class _ConsoleLoader:
    def __init__(self) -> None: ...
    def register(self, code: CodeType, source: str) -> None: ...
    def get_source_by_code(self, code: CodeType) -> t.Optional[str]: ...

class _InteractiveConsole(code.InteractiveInterpreter):
    locals: t.Dict[str, t.Any]
    loader: Any = ...
    compile: Any = ...
    more: bool = ...
    buffer: Any = ...
    def __init__(self, globals: t.Dict[str, t.Any], locals: t.Dict[str, t.Any]): ...
    def runsource(self, source: str, **kwargs: t.Any) -> str: ...
    def runcode(self, code: CodeType) -> None: ...
    def showtraceback(self) -> None: ...
    def showsyntaxerror(self, filename: t.Optional[str]=...) -> None: ...
    def write(self, data: str) -> None: ...

class Console:
    def __init__(self, globals: t.Optional[t.Dict[str, t.Any]]=..., locals: t.Optional[t.Dict[str, t.Any]]=...) -> None: ...
    def eval(self, code: str) -> str: ...
