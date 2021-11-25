import inspect
import typing
import warnings
from typing import Callable, List, Union

import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.types import Receive, Scope, Send

from simple_starlette.config import Config

from .exceptions import exception_handlers
from .route import Route, WebSocketRoute


class SimpleStarlette:
    # all route
    routes: List[Union[Route, WebSocketRoute]] = []

    # allow http method
    allow_methods = ["GET", "POST"]

    # starlette app
    simple_starlette_app: Starlette

    # config class
    config_class = Config

    def __init__(
        self,
        app_name: str,
        middleware: typing.Sequence[Middleware] = None,
        after_request_stack: typing.List[Callable] = None,
        before_reqeuest_stack: typing.List[Callable] = None,
    ) -> None:
        self.app_name = app_name

        # starlette middleware
        self.middleware = middleware if middleware else []

        # request event
        self.after_request_stack = after_request_stack if after_request_stack else []
        self.before_request_stack = (
            before_reqeuest_stack if before_reqeuest_stack else []
        )

        # app config
        self.config = self.make_config()

    def route(
        self,
        path,
        allow_methods: List[str] = None,
        websocket_route: bool = False,
        **options
    ):
        def register(cls: typing.Callable):
            if websocket_route:
                self.routes.append(WebSocketRoute(path, cls, **options))
                return

            # http route
            if inspect.isfunction(cls):
                if allow_methods is None:
                    raise Exception(
                        "endpoint is function , params: allow_methods is require !"
                    )
                self.routes.append(Route(path, cls, methods=allow_methods, **options))
            else:
                if allow_methods:
                    warnings.warn("endpoint is class, params: allow_methods is useless")
                methods = []
                for _m in self.allow_methods:
                    if getattr(cls, _m, None):
                        methods.append(_m.upper())
                if not methods:
                    raise Exception(
                        "not found any http method func in endpoint, {}".format(
                            cls.__class__.__name__
                        )
                    )
                self.routes.append(Route(path, cls, methods=methods, **options))

        return register

    def run(self, host: str = None, port: int = None, debug: bool = True, **options):
        # run mode
        options["debug"] = debug or self.config.get("DEBUG")
        # server listen port
        options["port"] = port or self.config.get("PORT", 9091)
        # server run host
        options["host"] = host or self.config.get("HOST", "127.0.0.1")

        uvicorn.run(self, **options)

    def gen_starlette_app(self):
        starlette_app = Starlette(
            routes=self.routes,
            middleware=self.middleware,
            debug=self.config.get("DEBUG", False),
            exception_handlers=exception_handlers,
        )
        if self.before_request_stack and self.after_request_stack:
            # http middleware
            @starlette_app.middleware("http")
            async def _(request: Request, call_next):
                for _f in self.before_request_stack:
                    await _f(request)
                response = await call_next(request)
                for _f in self.after_request_stack:
                    response = await _f(request, response)
                return response

        return starlette_app

    def make_config(self) -> dict:
        default_config = {"DEBUG": False, "ENV": None}
        return self.config_class(default_config)

    def before_request(self, func: Callable):
        """before request event"""
        self.before_request_stack.append(func)

    def after_request(self, func: Callable):
        """after request event"""
        self.after_request_stack.append(func)

    def get_routes_by_namespace(self, namespace: str):
        rv = []
        for _r in self.routes:
            if _r.path.startswith(namespace):
                rv.append(_r.path)
        return rv

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        starlette_app = getattr(self, "starlette_app", None)
        if not starlette_app:
            setattr(self, "starlette_app", self.gen_starlette_app())
        scope["app"] = self
        await starlette_app.middleware_stack(scope, receive, send)

    def __repr__(self) -> str:
        return "<SimpleStarlette '%s'>" % self.app_name
