from multiprocessing.context import SpawnProcess
from socket import socket
from typing import Any, Callable, List, Optional
from uvicorn.config import Config as Config

spawn: Any

def get_subprocess(config: Config, target: Callable[..., None], sockets: List[socket]) -> SpawnProcess: ...
def subprocess_started(config: Config, target: Callable[..., None], sockets: List[socket], stdin_fileno: Optional[int]) -> None: ...
