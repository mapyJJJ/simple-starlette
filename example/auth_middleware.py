# TokenAuthMiddleWareGenFunc 中间件使用示例
# 标准jwt token

from starlette.requests import Request
from starlette.responses import JSONResponse

from simple_starlette import SimpleStarlette
from simple_starlette.middleware.token_auth import (TokenAuthMiddleWareGenFunc,
                                                    register_skip_auth_routes)


async def check_is_login_process(payload: dict) -> bool:
    # 自定义 业务端 逻辑， 进一步操作如  查缓存 查表等 操作 ，固定返回 bool 代表 是否 通过验证
    print(f"entry: {payload}")
    return payload.get("test_is_login", False)


def custom_on_error(exc: Exception):
    # 自定义 验证未通过 时 返回值
    return JSONResponse({"message": "未登录", "status_code": 40003})


app = SimpleStarlette(
    __name__,
    middleware=[
        TokenAuthMiddleWareGenFunc(
            validate_process=check_is_login_process,
            on_error=custom_on_error,
        )
    ],
)

@app.route("/need_login_api")
async def ping(request: Request):
    return JSONResponse({"ping": "pong"})


@app.route("/set_session_api")
async def set_session_api(request: Request):
    # 登录模拟
    # 使用 request.auth 操作 session
    request.auth["test_is_login"] = True
    return JSONResponse({"is_success": True})


@app.route("/clear_session_api")
async def clear_session_api(request: Request):
    # 退出登录
    del request.auth["test_is_login"]
    return JSONResponse({"is_success": True})


register_skip_auth_routes(
    [set_session_api, clear_session_api]
)  #  排除一些不需要登陆的接口

app.run()
