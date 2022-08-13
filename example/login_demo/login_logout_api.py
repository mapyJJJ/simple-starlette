"""
简单的login logout小demo
GO LIVE login_logout_demo.html 到 5500端口
该服务启动在 9091 端口
用以验证 TokenAuto，Cors 中间件的使用
"""

from pydantic import Field
from starlette.requests import Request
from simple_starlette.args import BodyParams
from simple_starlette.responses import ResTypeEnum
from simple_starlette import SimpleStarlette, Response
from simple_starlette.middleware.token_auth import (
    TokenAuthMiddleWareGenFunc,
    register_skip_auth_routes,
)
from simple_starlette.middleware.cors import CorsMiddlewareGenFunc


def on_check_auth_is_error(exc):
    return Response(
        content={"is_auth": False, "message": "need to login"},
        res_type=ResTypeEnum.JSON,
        status_code=403,
    )


async def validate_auth(payload: dict) -> bool:
    if payload.get("user_id") == 1000:
        return True
    return False


app = SimpleStarlette(
    __name__,
    middleware=[
        TokenAuthMiddleWareGenFunc(
            token_name="auth_token",
            secret_conf="secret",
            path="/",
            expires=60 * 60,
            validate_process=validate_auth,
            on_error=on_check_auth_is_error,
        ),
        CorsMiddlewareGenFunc(
            allow_origins=["http://127.0.0.1:5500"],
            allow_credentials=True,
            allow_methods=("GET","POST",)
        )
    ],
)


@app.route("/login")
class Login:
    class LoginQuertArgs(BodyParams):
        name: str = Field(description="username")
        password: str = Field(description="password")

    async def post(self, request: Request, b: LoginQuertArgs):
        if b.name == "admin" and b.password == "123456":
            # login check success
            request.auth["user_id"] = 1000
            return Response(
                {"is_login": True},
                res_type=ResTypeEnum.JSON,
                status_code=200,
            )
        else:
            return Response(
                {"is_login": False},
                res_type=ResTypeEnum.JSON,
                status_code=403,
            )


@app.route("/logout")
class Logout:
    async def get(self, request: Request):
        del request.auth["user_id"]
        return Response(
            {"is_logout": True}, res_type=ResTypeEnum.JSON
        )

@app.route("/user/one")
class UserOne:
    async def get(self, request: Request):
        user_id = request.auth["user_id"]
        return Response({"user_id": user_id}, res_type=ResTypeEnum.JSON)

register_skip_auth_routes([Login])


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9091)
