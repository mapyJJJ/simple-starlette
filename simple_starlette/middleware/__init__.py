from abc import ABCMeta, abstractmethod
from typing import Any

from starlette.types import ASGIApp, Receive, Scope, Send


class MiddleWareConfig(dict):
    ...


class MiddlewareAbs(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, app: ASGIApp, **options) -> None:
        ...

    @abstractmethod
    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> Any:
        ...


middleware_config = MiddleWareConfig()
