import typing
from collections.abc import MutableMapping
from pathlib import Path
from typing import Any

class undefined: ...
class EnvironError(Exception): ...

class Environ(MutableMapping):
    def __init__(self, environ: typing.MutableMapping=...) -> None: ...
    def __getitem__(self, key: typing.Any) -> typing.Any: ...
    def __setitem__(self, key: typing.Any, value: typing.Any) -> None: ...
    def __delitem__(self, key: typing.Any) -> None: ...
    def __iter__(self) -> typing.Iterator: ...
    def __len__(self) -> int: ...

environ: Any
T: Any

class Config:
    environ: Any = ...
    file_values: Any = ...
    def __init__(self, env_file: typing.Union[str, Path]=..., environ: typing.Mapping[str, str]=...) -> None: ...
    @typing.overload
    def __call__(self, key: str, cast: typing.Type[T], default: T=...) -> T: ...
    @typing.overload
    def __call__(self, key: str, cast: typing.Type[str]=..., default: str=...) -> str: ...
    @typing.overload
    def __call__(self, key: str, cast: typing.Type[str]=..., default: T=...) -> typing.Union[T, str]: ...
    def get(self, key: str, cast: typing.Callable=..., default: typing.Any=...) -> typing.Any: ...