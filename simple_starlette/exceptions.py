# exceptions
# ~~~~~~~~~~~~~~~~~~~~~
import typing
from abc import ABCMeta, abstractstaticmethod
from typing import Any, Callable, TypeVar

from starlette.requests import Request

from simple_starlette.responses import Response, ResTypeEnum


class BaseException(Exception, metaclass=ABCMeta):
    def __init__(self, err_msg: Any = "", status_code: int = 400) -> None:
        self.err_msg = err_msg
        self.status_code = status_code

    @abstractstaticmethod
    async def exception_handle(request: Request, err: BaseException):
        Ellipsis


async def common_exception_handle(request: Request, err: BaseException):
    return Response(
        {"err_msg": err.err_msg, "err_code": err.status_code}, ResTypeEnum.JSON
    )


class RequestArgsResolvedError(BaseException):
    @staticmethod
    async def exception_handle(request: Request, err: BaseException):
        return await common_exception_handle(request, err)


class RequestArgsNoMatch(BaseException):
    @staticmethod
    async def exception_handle(request: Request, err: BaseException):
        return await common_exception_handle(request, err)


exception_handlers = typing.cast(
    typing.Dict[typing.Union[int, typing.Type[Exception]], typing.Callable],
    {
        RequestArgsNoMatch: RequestArgsNoMatch.exception_handle,
        RequestArgsResolvedError: RequestArgsResolvedError.exception_handle,
    },
)


T = TypeVar("T")


def register_exception(cls: T, exception_handle: Callable) -> T:
    exception_handlers.update({cls: exception_handle})
    return cls
