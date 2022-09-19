# 其他sentry-sdk用法参考
# https://docs.sentry.io/platforms/python/

import operator
from simple_starlette import Request
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.middleware import Middleware
from simple_starlette import SimpleStarlette
import sentry_sdk.hub

sentry_sdk.hub.init(dsn="xxxxxxxxxxxxxxxxxx")  # 此处放入sentry dsn地址
app = SimpleStarlette(
    __name__, middleware=[Middleware(SentryAsgiMiddleware)]
)


@app.route("/raise_error", allow_methods=["GET"])
async def raise_error(request: Request):
    return 1 / 0


if __name__ == "__main__":
    app.run()
