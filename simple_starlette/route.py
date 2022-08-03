# route.py
# ~~~~~~~~~~~~

import inspect
import typing

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse, Response
from starlette.routing import Route as _Route
from starlette.routing import WebSocketRoute as _WebSocketRoute
from starlette.routing import compile_path, get_name, websocket_session
from starlette.types import ASGIApp, Receive, Scope, Send

from simple_starlette.middleware.token_auth import TokenAuth
from simple_starlette.types import Route as _RouteT

from .dispatch_request import dispatch_request
from .exceptions import RequestArgsResolvedError

try:
    import contextvars  # > python 3.6 +
except ImportError:
    contextvars = None  # type: ignore


def request_response(func: typing.Callable) -> ASGIApp:
    async def app(scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope, receive=receive, send=send)
        content_type = request.headers.get("Content-Type")
        _d = {}
        if request.query_params:
            _d["query"] = request.query_params
        if request.method == "POST":
            try:
                if (
                    content_type
                    == "application/x-www-form-urlencoded"
                ):
                    data = await request.form()
                elif content_type == "application/json":
                    data = await request.json()
                else:
                    raise TypeError(
                        "`content_type is` `%s`, not supported"
                        % content_type
                    )
                _d["body"] = data
            except Exception as e:
                raise RequestArgsResolvedError(
                    err_msg="Request parameter error, could not be resolved, error: {}".format(
                        str(e)
                    ),
                    err_code=4041,
                )
        # dispatch request
        setattr(request, "data", _d)
        # 分发至业务视图函数中处理
        response = typing.cast(
            Response, await dispatch_request(func, request, _d)
        )
        # save_session
        response = await TokenAuth.save_session(request, response)

        await response(scope, receive, send)

    return app


class Route(_Route):
    def __init__(
        self,
        path: str,
        endpoint: typing.Callable,
        *,
        methods: typing.List[str] = [],
        name: str = None,
        include_in_schema: bool = True,
        include_name: str = None,
    ) -> None:
        """ """

        assert path.startswith(
            "/"
        ), "Routed paths must start with '/'"

        self.path = path
        self.endpoint = endpoint
        self.name = get_name(endpoint) if name is None else name
        self.include_in_schema = include_in_schema

        # endpoint is func or method
        self.app = request_response(endpoint)

        self.include_name = include_name

        self.methods = [method.upper() for method in methods]
        # if "GET" in self.methods:
        #     self.methods.append("HEAD")

        (
            self.path_regex,
            self.path_format,
            self.param_convertors,
        ) = compile_path(path)

    async def handle(
        self, scope: Scope, receive: Receive, send: Send
    ) -> None:
        if self.methods and scope["method"] not in self.methods:
            if "app" in scope:
                raise HTTPException(status_code=405)
            else:
                response = PlainTextResponse(
                    "Method Not Allowed", status_code=405
                )
            await response(scope, receive, send)
        else:
            await self.app(scope, receive, send)


class WebSocketRoute(_WebSocketRoute):
    def __init__(
        self,
        path: str,
        endpoint: typing.Callable,
        *,
        name: str = None,
    ) -> None:
        assert path.startswith(
            "/"
        ), "Routed paths must start with '/'"
        self.path = path
        self.endpoint = endpoint
        self.name = get_name(endpoint) if name is None else name

        self.app = request_response(endpoint)

        if inspect.isfunction(endpoint) or inspect.ismethod(endpoint):
            # Endpoint is function or method. Treat it as `func(websocket)`.
            self.app = websocket_session(endpoint)
        else:
            # Endpoint is a class. Treat it as ASGI.
            if not hasattr(endpoint, "handle"):
                raise Exception(
                    "websocker endpoint is class, the `handle` func is require"
                )
            self.app = websocket_session(getattr(endpoint, "handle"))

        (
            self.path_regex,
            self.path_format,
            self.param_convertors,
        ) = compile_path(path)
