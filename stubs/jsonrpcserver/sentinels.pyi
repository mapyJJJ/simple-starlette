from typing import Any

class Sentinel:
    name: Any = ...
    def __init__(self, name: str) -> None: ...

NOCONTEXT: Any
NODATA: Any
NOID: Any
