# types.py
# ~~~~~~~~~~

import typing

from starlette.middleware import Middleware
from starlette.types import Receive, Scope, Send
from typing_extensions import TypeAlias

T = typing.TypeVar("T")
ArgsT = typing.TypeVar("ArgsT", bound=object)
SimpleApp = typing.Callable[
    [Scope, Receive, Send], typing.Awaitable[None]
]
_L_M: TypeAlias = typing.Optional[typing.List[Middleware]]


class Route:
    path: str
    endpoint: typing.Callable
    name: typing.Optional[str] = None
    include_in_schema: bool
