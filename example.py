from starlette.requests import Request

from simple_starlette import (SimpleStarlette, common_exception_handle,
                              register_exception)
from simple_starlette.exceptions import SimpleException

app = SimpleStarlette(__name__)


@register_exception(404)
class NotFound:
    @staticmethod
    async def exception_handle(request: Request, exc):
        err = SimpleException(err_msg="路由不存在", err_code=4040)
        return await common_exception_handle(request, err)


@register_exception()
class CustomError(SimpleException):
    @staticmethod
    async def exception_handle(request: Request, err: "SimpleException"):
        return await common_exception_handle(request, err)


@app.route("/test", allow_methods=["GET"])
async def test(request: Request):
    raise CustomError(err_msg="自定义错误", err_code=10001)


app.run()