from .exceptions import RequestArgsResolvedError
import typing
from enum import Enum

from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route as _Route
from starlette.routing import compile_path, get_name
from starlette.types import ASGIApp, Receive, Scope, Send

from .dispatch_request import dispatch_request

try:
    import contextvars
except ImportError:
    contextvars = None  # type: ignore


# allow http method
allow_methods = ["get", "post"]

# all routes
routes = []


def request_response(func: typing.Callable) -> ASGIApp:
    async def app(scope: Scope, receive: Receive, send: Send) -> None:
        request = Request(scope, receive=receive, send=send)
        content_type = request.headers.get("Content-Type")
        if request.method == "GET":
            data = request.query_params
        else:
            try:
                if content_type == "application/x-www-form-urlencoded":
                    data = await request.form()
                else:
                    data = await request.json()
            except Exception as e:
                raise RequestArgsResolvedError(
                    err_msg="Request parameter error, could not be resolved, {str(e)}",
                    status_code=4041,
                )
        # dispatch request
        response = await dispatch_request(func, request, data)
        await response(scope, receive, send)

    return app


class Route(_Route):
    def __init__(
        self,
        path: str,
        endpoint: typing.Callable,
        *,
        methods: typing.List[str] = None,
        name: str = None,
        include_in_schema: bool = True,
    ) -> None:
        """ """

        assert path.startswith("/"), "Routed paths must start with '/'"

        self.path = path
        self.endpoint = endpoint
        self.name = get_name(endpoint) if name is None else name
        self.include_in_schema = include_in_schema

        # endpoint is func or method
        self.app = request_response(endpoint)

        self.methods = {method.upper() for method in methods}
        if "GET" in self.methods:
            self.methods.add("HEAD")

        self.path_regex, self.path_format, self.param_convertors = compile_path(path)

    async def handle(self, scope: Scope, receive: Receive, send: Send) -> None:
        if self.methods and scope["method"] not in self.methods:
            if "app" in scope:
                raise HTTPException(status_code=405)
            else:
                response = PlainTextResponse("Method Not Allowed", status_code=405)
            await response(scope, receive, send)
        else:
            await self.app(scope, receive, send)
