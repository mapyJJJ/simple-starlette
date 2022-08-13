# 标准jwt token
# TokenAuthMiddleWareGenFunc , Cors 中间件使用示例

from starlette.requests import Request
from starlette.responses import JSONResponse

from simple_starlette import SimpleStarlette, Response, ResTypeEnum
from simple_starlette.middleware.token_auth import (TokenAuthMiddleWareGenFunc,
                                                    register_skip_auth_routes)
from simple_starlette.middleware.cors import CorsMiddlewareGenFunc


async def check_is_login_process(payload: dict) -> bool:
    # 自定义 业务端 逻辑， 进一步操作如  查缓存 查表等 操作 ，固定返回 bool 代表 是否 通过验证
    print(f"entry: {payload}")
    return payload.get("test_is_login", False)


def custom_on_error(exc: Exception):
    # 自定义 验证未通过 时 返回值
    return Response({"message": "未登录"}, ResTypeEnum.JSON, status_code=403)


app = SimpleStarlette(
    __name__,
    middleware=[
        TokenAuthMiddleWareGenFunc(
            validate_process=check_is_login_process,
            on_error=custom_on_error,
            expires=60 * 60,
            httponly=True
        ),
        CorsMiddlewareGenFunc(
            allow_origins=["http://127.0.0.1:5500"],
            allow_credentials=True,
            allow_methods=("GET","POST",)
        )
    ],
)

@app.route("/need_login_api", allow_methods=["GET"])
async def ping(request: Request):
    _ = request.auth.get("test_is_login")
    headers={"Access-Control-Allow-Credentials": "true"}
    return JSONResponse({"ping": "pong"},headers=headers)


@app.route("/login", allow_methods=["GET"])
async def set_session_api(request: Request):
    # 登录模拟
    # 使用 request.auth 操作 session
    request.auth["test_is_login"] = True
    return JSONResponse({"is_login": True})

@app.route("/logout", allow_methods=["GET"])
async def clear_session_api(request: Request):
    # 退出登录
    del request.auth["test_is_login"]
    return JSONResponse({"is_logout": True})

register_skip_auth_routes(
    [set_session_api, clear_session_api]
)  #  排除一些不需要登陆的接口

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=9091)
