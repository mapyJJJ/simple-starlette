from abc import ABCMeta, abstractmethod
from typing import Any, NewType

from starlette.types import ASGIApp, Receive, Scope, Send

_ASGIAPP = NewType("_ASGIAPP", ASGIApp)
_Receive = NewType("_Receive", Receive)
_Send = NewType("_Send", Send)
_Scope = NewType("_Scope", Scope)

class MiddleWareConfig(dict):
    ...


class MiddlewareAbs(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, app: _ASGIAPP, **options) -> None:
        ...

    @abstractmethod
    async def __call__(
        self, scope: _Scope, receive: _Receive, send: _Send
    ) -> Any:
        ...


middleware_config = MiddleWareConfig()
