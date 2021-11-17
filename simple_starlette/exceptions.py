from simple_starlette.responses import ResTypeEnum, Response
from typing import Any, Dict, TypeVar
import typing
from starlette.requests import Request


class BaseException(Exception):
    def __init__(self, msg: Any = "", status_code: int = 400) -> None:
        self.msg = msg
        self.status_code = status_code

    async def _handle(self, request: Request):
        return Response(
            {"err_msg": self.msg, "err_code": self.status_code}, ResTypeEnum.JSON
        )


class RequestArgsResolvedError(BaseException):
    Ellipsis


class RequestArgsNoMatch(BaseException):
    Ellipsis


T = TypeVar("T")

exception_handlers = typing.cast(
    typing.Dict[typing.Union[int, typing.Type[Exception]], typing.Callable],
    {
        RequestArgsNoMatch: RequestArgsNoMatch._handle,
        RequestArgsResolvedError: RequestArgsResolvedError._handle,
    },
)


def register_exception(self, cls: T, handle_name: str) -> T:
    exception_handlers.update({cls: getattr(cls, handle_name, "not found handle")})
    return cls
