# types.py
# ~~~~~~~~~~

import typing

from starlette.types import Receive, Scope, Send

ArgsT = typing.TypeVar("ArgsT", bound=object)
SimpleApp = typing.Callable[[Scope, Receive, Send], typing.Awaitable[None]]
