# --req-hook--
"""
使用before_request , after_request钩子（中间件）
"""


import time

from starlette.requests import Request

from simple_starlette import Response, ResTypeEnum, SimpleStarlette, g

app = SimpleStarlette(__name__)


@app.before_request
async def _do_before_request(request):
    g.start_time = time.time()
    return request


@app.after_request
async def _do_after_request(request, response):
    process_time = time.time() - g.start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.route("/test", ["GET"])
async def test(request: Request):
    return Response(str(request.url), ResTypeEnum.TEXT)


if __name__ == "__main__":
    app.run()
