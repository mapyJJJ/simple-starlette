from distutils.errors import DistutilsError
from typing import Any

class UnpickleableException(Exception):
    @staticmethod
    def dump(type: Any, exc: Any): ...

class ExceptionSaver:
    def __enter__(self): ...
    def __exit__(self, type: Any, exc: Any, tb: Any): ...
    def resume(self) -> None: ...

def run_setup(setup_script: Any, args: Any): ...

class AbstractSandbox:
    def __init__(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def run(self, func: Any): ...

class DirectorySandbox(AbstractSandbox):
    write_ops: Any = ...
    def __init__(self, sandbox: Any, exceptions: Any = ...) -> None: ...
    def tmpnam(self) -> None: ...
    def open(self, file: Any, flags: Any, mode: int = ..., *args: Any, **kw: Any): ...

class SandboxViolation(DistutilsError):
    tmpl: Any = ...