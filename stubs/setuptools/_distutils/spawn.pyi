from distutils.errors import DistutilsPlatformError as DistutilsPlatformError
from typing import Any, Optional

def spawn(cmd: Any, search_path: int = ..., verbose: int = ..., dry_run: int = ..., env: Optional[Any] = ...) -> None: ...
def find_executable(executable: Any, path: Optional[Any] = ...): ...
