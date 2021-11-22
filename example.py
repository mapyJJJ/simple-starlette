from simple_starlette.exceptions import SimpleException
from starlette.requests import Request
from simple_starlette import (
    SimpleStarlette,
    register_exception,
    common_exception_handle,
)

app = SimpleStarlette(__name__)


@register_exception
class TestError(SimpleException):
    @staticmethod
    async def exception_handle(request: Request, err: "SimpleException"):
        return await common_exception_handle(request, err)


@app.route("/test")
async def test(request: Request):
    raise TestError(err_msg="test error", status_code=4000)


app.run()
