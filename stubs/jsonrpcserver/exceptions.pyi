from .sentinels import NODATA as NODATA
from typing import Any

class JsonRpcError(Exception):
    def __init__(self, code: int, message: str, data: Any=...) -> None: ...
