"""
This type stub file was generated by pyright.
"""

from types import TracebackType
from typing import Any, Text, Type, Union
from redis.client import Redis

_TokenValue = Union[bytes, Text]
class Lock:
    def __init__(self, redis: Redis[Any], name: str, timeout: None | int | float = ..., sleep: float = ..., blocking: bool = ..., blocking_timeout: bool | None = ..., thread_local: bool = ...) -> None:
        ...
    
    def register_scripts(self) -> None:
        ...
    
    def __enter__(self) -> Lock:
        ...
    
    def __exit__(self, exc_type: Type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> bool | None:
        ...
    
    def acquire(self, blocking: bool | None = ..., blocking_timeout: None | int | float = ..., token: _TokenValue | None = ...) -> bool:
        ...
    
    def do_acquire(self, token: _TokenValue) -> bool:
        ...
    
    def locked(self) -> bool:
        ...
    
    def owned(self) -> bool:
        ...
    
    def release(self) -> None:
        ...
    
    def do_release(self, expected_token: _TokenValue) -> None:
        ...
    
    def extend(self, additional_time: int | float, replace_ttl: bool = ...) -> bool:
        ...
    
    def do_extend(self, additional_time: int | float, replace_ttl: bool) -> bool:
        ...
    
    def reacquire(self) -> bool:
        ...
    
    def do_reacquire(self) -> bool:
        ...
    


