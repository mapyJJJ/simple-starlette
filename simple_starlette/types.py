# types.py
# ~~~~~~~~~~

import typing
import pydantic
from starlette.types import Receive, Scope, Send


ArgsT = typing.TypeVar("ArgsT", bound=pydantic.BaseModel)
SimpleApp = typing.Callable[[Scope, Receive, Send], typing.Awaitable[None]]
