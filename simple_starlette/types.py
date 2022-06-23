# types.py
# ~~~~~~~~~~

import typing

from starlette.types import Receive, Scope, Send

T = typing.TypeVar("T")
ArgsT = typing.TypeVar("ArgsT", bound=object)
SimpleApp = typing.Callable[
    [Scope, Receive, Send], typing.Awaitable[None]
]


class Route:
    path: str
    endpoint: typing.Callable
    name: typing.Optional[str] = None
    include_in_schema: bool
