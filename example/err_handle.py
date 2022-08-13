#--err--
# 处理全局报错

from starlette.requests import Request

from simple_starlette import (SimpleStarlette, common_exception_handle,
                              register_exception)
from simple_starlette.exceptions import SimpleException

app = SimpleStarlette(__name__)


@register_exception(404)
class NotFound:
    @staticmethod
    async def exception_handle(request: Request, exc):
        err = SimpleException(error="路由不存在", err_code=404)
        return await common_exception_handle(request, err)


@register_exception()
class CustomError(SimpleException):
    @staticmethod
    async def exception_handle(request: Request, err: "SimpleException"):
        return await common_exception_handle(request, err)


@app.route("/test", allow_methods=["GET"])
async def test(request: Request):
    # 如果是断点调试模式，这个Exception会先被编辑器捕获
    # 要查看实际返回，请不要通过 编辑器 或 IDE 的debug调试来启动服务
    raise CustomError(error="服务器错误", err_code=401)
    return


if __name__ == "__main__":
    """
     curl localhost:9091/test
     {"err_msg":"自定义错误","err_code":10001}

    curl localhost:9091/test1
    {"err_msg":"路由不存在","err_code":4040}

    """
    app.run()