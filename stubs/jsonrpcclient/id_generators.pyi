from typing import Iterator

def decimal(start: int=...) -> Iterator[int]: ...
def hexadecimal(start: int=...) -> Iterator[str]: ...
def random(length: int=..., chars: str=...) -> Iterator[str]: ...
def uuid() -> Iterator[str]: ...
