from typing import Any, Optional

class TextFile:
    default_options: Any = ...
    filename: Any = ...
    file: Any = ...
    current_line: int = ...
    linebuf: Any = ...
    def __init__(self, filename: Optional[Any] = ..., file: Optional[Any] = ..., **options: Any) -> None: ...
    def open(self, filename: Any) -> None: ...
    def close(self) -> None: ...
    def gen_error(self, msg: Any, line: Optional[Any] = ...): ...
    def error(self, msg: Any, line: Optional[Any] = ...) -> None: ...
    def warn(self, msg: Any, line: Optional[Any] = ...) -> None: ...
    def readline(self): ...
    def readlines(self): ...
    def unreadline(self, line: Any) -> None: ...