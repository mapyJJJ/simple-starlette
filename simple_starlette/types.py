import typing

from starlette.types import Receive, Scope, Send


SimpleApp = typing.Callable[[Scope, Receive, Send], typing.Awaitable[None]]
