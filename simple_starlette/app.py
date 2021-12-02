#   app.py
# ~~~~~~~~~~~

import inspect
import typing
import warnings
from typing import Any, Callable, Dict, List

import uvicorn
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.types import Receive, Scope, Send

from simple_starlette.config import Config

from .exceptions import exception_handlers
from .route import Route, WebSocketRoute


class SimpleStarlette:
    """
    SimpleStarlette base on Starlette
    Did some more friendly to developers of functional adaptation
    simple_starlette are designed to facilitate quick used to create Web Project
    """

    config_class = Config

    routes: Dict[str, Route] = {}

    allow_methods = ["GET", "POST"]

    simple_starlette_app: Starlette

    websocket_routes: Dict[str, WebSocketRoute] = {}

    def __init__(
        self,
        app_name: str,
        middleware: typing.Sequence[Middleware] = None,
        after_request_stack: typing.List[Callable] = None,
        before_reqeuest_stack: typing.List[Callable] = None,
    ) -> None:
        """init simplestarlette app

        create app
        ```
            from simple_starlette import SimpleStarlette
            app = SimpleStarlette(__name__)
        ```


        Keyword arguments:
        :app_name
            The name identifies the distinction between different instances of the APP
        :middleware
            starlette middleware, look startlette.middlewares/
        :after_request_stack
            do something after request handle complete
        :before_reqeuest_stack
            do something before receive request

        """
        self.app_name = app_name

        self.config = self.make_config()

        self.middleware = middleware if middleware else []

        self.after_request_stack = after_request_stack if after_request_stack else []

        self.before_request_stack = (
            before_reqeuest_stack if before_reqeuest_stack else []
        )

    def route(
        self,
        path: str,
        websocket_route: bool = False,
        allow_methods: List[str] = ["GET", "POST"],
        **options,
    ):
        """register api route

        Keyword arguments:
        :path
            route path
        :websocket_route
            set True if register a websocket api
        :allow_methods
            Request methods that allow use,
            when using the Functions view custom view method,
            this parameter is required
        """

        def register(cls: typing.Callable):
            if websocket_route:
                assert (
                    path not in self.websocket_routes
                ), f"same path `{path}` has been register"
                self.websocket_routes[path] = WebSocketRoute(path, cls, **options)
                return

            if inspect.isfunction(cls):
                self.routes[path] = Route(path, cls, methods=allow_methods, **options)

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
                self.routes[path] = Route(path, cls, methods=methods, **options)
            return

        return register

    def run(self, host: str = None, port: int = None, debug: bool = True, **options):
        """Get up and running by uvicorn server
        you need to provide some parameters, ex: `host`, `port`...

        Through the introduction of configuration parameters as follows:

        ```
            from simple_starlette import SimpleStarlette

            app = SimpleStarlette(__name__)

            app.config["host"] = "0.0.0.0"
            app.config["port"] = 5000
        ```
        """

        options["debug"] = debug or self.config.get("DEBUG")
        options["port"] = port or self.config.get("PORT", 9091)
        options["host"] = host or self.config.get("HOST", "127.0.0.1")

        uvicorn.run(self, **options)

    def rquest_hook(self, starlette_app):
        """use starlette http middleware"""

        if self.before_request_stack and self.after_request_stack:

            @starlette_app.middleware("http")
            async def _(request, call_next):
                for _f in self.before_request_stack:
                    await _f(request)
                response = await call_next(request)
                for _f in self.after_request_stack:
                    response = await _f(request, response)
                return response

        return

    def gen_starlette_app(self):
        """gen starlette app"""

        if hasattr(self, "starlette_app"):
            return getattr(self, "starlette_app")

        starlette_app = Starlette(
            middleware=self.middleware,
            exception_handlers=exception_handlers,
            debug=self.config.get("DEBUG", False),
            routes=list([r for r in self.iter_all_routes()]),
        )
        self.rquest_hook(starlette_app)
        setattr(self, "starlette_app", starlette_app)
        return starlette_app

    def make_config(self):
        """return config object"""
        default_config = {"DEBUG": False, "ENV": None}
        return self.config_class(default_config)

    def before_request(self, func: Callable):
        """before request event"""
        self.before_request_stack.append(func)

    def after_request(self, func: Callable):
        """after request event"""
        self.after_request_stack.append(func)

    def get_paths_by_namespace(self, namespace: str):
        """
        if path startwith namespace , it will be return
        """
        rv = []
        for r in self.iter_all_routes():
            if r.path.startswith(namespace):
                rv.append(r.path)
        return rv

    def iter_all_routes(self):
        for _, r in self.routes.items():
            yield r
        for _, r in self.websocket_routes.items():
            yield r

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        scope["app"] = self
        starlette_app = self.gen_starlette_app()
        await starlette_app.middleware_stack(scope, receive, send)

    def __repr__(self) -> str:
        return "<SimpleStarlette '%s'>" % self.app_name
