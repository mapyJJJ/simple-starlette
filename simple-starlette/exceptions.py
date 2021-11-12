from typing import TypeVar
from starlette.responses import JSONResponse
from starlette.requests import Request


class BaseException(Exception):
    @staticmethod
    async def common_handle(request: Request, e: "BaseException"):
        return JSONResponse({"err_msg": e.msg})

    handle_func = common_handle

    def __init__(self, msg: str = "", status_code: int = 500) -> None:
        self.msg = msg
        self.status_code = status_code


class RequestArgsError(BaseException):
    # 请求参数解析错误
    def __init__(self, msg: str = "", status_code: int = 400) -> None:
        self.msg = "请求参数解析错误,请检查格式"
        self.status_code = status_code


T = TypeVar("T")

exception_handlers = {RequestArgsError: RequestArgsError.handle_func}


class RegisterExceptionHandlers:
    def register_exception(self, cls: T) -> T:
        exception_handlers.update({cls: getattr(cls, "handle_func", None)})
        return cls
