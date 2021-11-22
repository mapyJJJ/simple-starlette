import typing
from typing import Any, Callable, List
from starlette.requests import Request

import uvicorn
from starlette.applications import Starlette
from starlette.types import Receive, Scope, Send
from starlette.middleware import Middleware

from .exceptions import exception_handlers
from .route import Route


class SimpleStarlette:
    # all route
    routes = []

    # allow http method
    allow_methods = ["GET", "POST"]

    def __init__(
        self,
        app_name: str,
        middleware: typing.Sequence[Middleware] = None,
        after_request_stack: typing.List[Callable] = None,
        before_reqeuest_stack: typing.List[Callable] = None,
    ) -> None:
        self.app_name = app_name
        self.middleware = middleware if middleware else []
        self.after_request_stack = after_request_stack if after_request_stack else []
        self.before_request_stack = (
            before_reqeuest_stack if before_reqeuest_stack else []
        )

        self.simple_starlette_app = None

    def route(self, path, **options):
        def register(cls: typing.Callable):
            methods = []
            for _m in self.allow_methods:
                if getattr(cls, _m, None):
                    methods.append(_m.upper())
            self.routes.append(Route(path, cls, methods=methods, **options))

        return register

    def register_route(self, path, cls: typing.Callable, methods: List[str], **options):
        self.routes.append(Route(path, cls, methods=methods, **options))
        return

    def run(self, host: str = None, port: int = None, debug: bool = True, **options):
        # run mode
        options["debug"] = debug
        # server listen port
        options["port"] = port or 9091
        # server run host
        options["host"] = host or "127.0.0.1"

        uvicorn.run(self, **options)

    def gen_starlette_app(self, debug=False, **kwds: Any) -> Any:
        self.simple_starlette_app = Starlette(
            debug=debug,
            routes=self.routes,
            middleware=self.middleware,
            exception_handlers=exception_handlers,
            **kwds
        )
        if self.before_request_stack and self.after_request_stack:

            @self.simple_starlette_app.middleware("http")
            async def process_func(request: Request, call_next):
                for _f in self.before_request_stack:
                    await _f(request)
                response = await call_next(request)
                for _f in self.after_request_stack:
                    response = await _f(request, response)
                return response

        return self.simple_starlette_app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if not self.simple_starlette_app:
            self.simple_starlette_app = self.gen_starlette_app()
        scope["app"] = self
        await self.simple_starlette_app.middleware_stack(scope, receive, send)

    def before_request(self, func: Callable):
        self.before_request_stack.append(func)

    def after_request(self, func: Callable):
        self.after_request_stack.append(func)

    def __repr__(self) -> str:
        return "<SimpleStarlette '%s'>" % self.app_name
