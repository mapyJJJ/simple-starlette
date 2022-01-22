# exceptions handler
# ~~~~~~~~~~~~~~~~~~~

import typing
from abc import ABCMeta, abstractstaticmethod
from typing import Any

from starlette.requests import Request

from simple_starlette.responses import Response, ResTypeEnum
from simple_starlette.types import T


class SimpleException(Exception, metaclass=ABCMeta):
    def __init__(self, err_msg: Any = "", err_code: int = 400) -> None:
        self.err_msg = err_msg
        self.err_code = err_code

    @abstractstaticmethod
    async def exception_handle(request, err: "SimpleException"):
        Ellipsis


async def common_exception_handle(request: Request, err: SimpleException):
    return Response(
        {"err_msg": err.err_msg, "err_code": err.err_code}, ResTypeEnum.JSON
    )


class RequestArgsResolvedError(SimpleException):
    @staticmethod
    async def exception_handle(request: Request, err: SimpleException):
        return await common_exception_handle(request, err)


class RequestArgsNoMatch(SimpleException):
    @staticmethod
    async def exception_handle(request: Request, err: SimpleException):
        return await common_exception_handle(request, err)


exception_handlers = typing.cast(
    typing.Dict[typing.Union[int, typing.Type[Exception], T], typing.Callable],
    {
        RequestArgsNoMatch: RequestArgsNoMatch.exception_handle,
        RequestArgsResolvedError: RequestArgsResolvedError.exception_handle,
    },
)


def register_exception(code: int = None):
    def decorator(cls: T) -> T:
        exception_handlers.update(
            {code if code else cls: getattr(cls, "exception_handle")}
        )
        return cls

    return decorator
