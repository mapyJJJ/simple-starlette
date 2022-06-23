import typing

import jwt
from jwt.exceptions import PyJWTError
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp, Receive, Scope, Send

from simple_starlette.responses import JSONResponse
from simple_starlette.types import Route

from . import middleware_config


class UnauthorizedException(Exception):
    def __init__(
        self, message: str = "Unauthorized", status_code: int = 40003
    ) -> None:
        self.message = message
        self.status_code = status_code


class Session(dict):
    is_modified = False

    def on_update(self):
        self.is_modified = True

    def pop(self, key):
        self.on_update()
        try:
            return super().pop(key)
        except KeyError:
            pass

    def __delitem__(self, v) -> None:
        self.on_update()
        try:
            return super().__delitem__(v)
        except KeyError:
            pass

    def __setitem__(self, k, v) -> None:
        self.on_update()
        return super().__setitem__(k, v)


all_skip_auth_paths = set()


def register_skip_auth_routes(
    routes: typing.List[Route],
):
    all_skip_auth_paths.update(set(_r.path for _r in routes))


class TokenAuth:
    def __init__(
        self,
        app: ASGIApp,
        token_name: str = "token",
        secret_conf: str = "secret",
        algorithm_conf: str = "HS256",
        validate_process: typing.Callable[
            [typing.Dict], typing.Coroutine
        ] = None,
        on_error: typing.Callable = None,
        max_age: int = None,
        expires: int = None,
        path: str = "/",
        domain: str = None,
        secure: bool = False,
        httponly: bool = False,
        samesite: str = "lax",
    ) -> None:
        self.app = app
        self.token_name = middleware_config[
            "token_auth.token_name"
        ] = token_name
        self.validate_process = validate_process
        self.cookies_params = middleware_config[
            "token_auth.cookies_params"
        ] = dict(
            max_age=max_age,
            expires=expires,
            path=path,
            domain=domain,
            secure=secure,
            httponly=httponly,
            samesite=samesite,
        )
        self.on_error = on_error or self.default_on_error
        self.jwt_decode = lambda token: jwt.decode(
            token, secret_conf, algorithms=[algorithm_conf]
        )
        self.jwt_encode = middleware_config[
            "token_auth.jwt_encode"
        ] = lambda raw_payload: jwt.encode(
            raw_payload, secret_conf, algorithm=algorithm_conf
        )

    @classmethod
    async def save_session(
        cls, request: Request, response: Response
    ) -> Response:
        try:
            assert isinstance(request.auth, Session)
            session = request.auth
        except AssertionError:
            return response
        if not session.is_modified:
            return response
        response.set_cookie(
            middleware_config["token_auth.token_name"],
            middleware_config["token_auth.jwt_encode"](request.auth),
            **middleware_config["token_auth.cookies_params"],
        )
        return response

    def find_cookie(
        self, headers: typing.List
    ) -> typing.Optional[typing.Dict[str, str]]:
        cookies = dict()
        cookie_str: str = ""
        for _k, _v in reversed(headers):
            if _k == b"cookie":
                cookie_str = _v.decode("utf-8")
        if cookie_str:
            for _item in cookie_str.split(";"):
                _k, _, _v = _item.partition("=")
                cookies[_k.replace(" ", "")] = _v.replace(" ", "")
            return cookies
        return None

    async def open_session(
        self, scope: Scope, receive: Receive, send: Send
    ):
        error_response = None
        auth_payload = {}
        blank_cookies = {}

        cookies = (
            self.find_cookie(scope.get("headers", []))
            or blank_cookies
        )
        if token := cookies.get(self.token_name):
            try:
                auth_payload = self.jwt_decode(token)
                if self.validate_process:
                    if not await self.validate_process(auth_payload):
                        error_response = self.on_error(
                            UnauthorizedException(
                                message="not passed custom login check"
                            )
                        )
            except PyJWTError as e:
                error_response = self.on_error(
                    UnauthorizedException()
                )
        else:
            error_response = self.on_error(
                UnauthorizedException(message="need to login")
            )

        if error_response and scope["path"] in all_skip_auth_paths:
            error_response = None

        if auth_payload:
            session = Session(**auth_payload)
        else:
            session = Session()
        scope["auth"] = session

        return error_response

    async def __call__(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        if scope["type"] not in ["http", "websocket"]:
            await self.app(scope, receive, send)
            return

        error_response = await self.open_session(scope, receive, send)
        if error_response:
            return await error_response(scope, receive, send)

        await self.app(scope, receive, send)

    @staticmethod
    def default_on_error(exc=UnauthorizedException()):
        return JSONResponse(
            {
                "message": exc.message,
                "status_code": exc.status_code,
            }
        )


def TokenAuthMiddleWareGenFunc(
    token_name: str = "token",
    secret_conf: str = "secret",
    algorithm_conf: str = "HS256",
    validate_process: typing.Callable[
        [typing.Dict], typing.Coroutine
    ] = None,
    on_error: typing.Callable = None,
    expires: int = None,
    path: str = "/",
    domain: str = None,
    secure: bool = False,
    httponly: bool = False,
    **options,
):
    options["token_name"] = token_name
    options["secret_conf"] = secret_conf
    options["algorithm_conf"] = algorithm_conf
    options["validate_process"] = validate_process
    options["on_error"] = on_error
    options["expires"] = expires
    options["path"] = path
    options["domain"] = domain
    options["secure"] = secure
    options["httponly"] = httponly
    return Middleware(TokenAuth, **options)
