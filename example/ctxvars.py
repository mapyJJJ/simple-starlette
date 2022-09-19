# ctxvars
# flask继承下来的思想，
# 除了提供上下文级别的全局变量，最大的好出是做视图解耦，
# 1, 防止复杂的结构目录下 引起不必要的循环引用
# 2, 避免了参数长传
# --------------

import json
import typing
from simple_starlette import (
    g,
    request,
    current_app,
    SimpleStarlette,
    Request,
)
from simple_starlette.responses import ResTypeEnum, Response

app = SimpleStarlette(__name__)


@app.route("/")
class Index:
    async def get(
        self, _: Request
    ):  # 可以不必显式接收request对象，直接获取全局的request对象
        print(g.CONTEXT_CONFIG)
        g.CONTEXT_CONFIG = {"k": "v"}  # 从应用上下文中定义的全局变量，生命周期等同当前请求
        print(g.CONTEXT_CONFIG)
        print(request.url)
        return Response("ok", ResTypeEnum.TEXT)

if __name__ == "__main__":
    app.run()
