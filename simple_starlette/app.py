import typing
import uvicorn
from typing import Any
from .route import Route
from .exceptions import exception_handlers
from starlette.applications import Starlette
from starlette.types import Receive, Scope, Send


class SimpleStarlette:
    # all route
    routes = []

    # allow http method
    allow_methods = ["GET", "POST"]

    def __init__(self, app_name: str) -> None:
        self.app_name = app_name

        self.simple_starlette_app = None

    def route(self, path, **options):
        def register(cls: typing.Callable):
            methods = []
            for _m in self.allow_methods:
                if getattr(cls, _m, None):
                    methods.append(_m.upper())
            self.routes.append(Route(path, cls, methods=methods, **options))

        return register

    def run(self, host: str = None, port: int = None, debug: bool = True, **options):
        # run mode
        options["debug"] = debug
        # server listen port
        options["port"] = port or 9091
        # server run host
        options["host"] = host or "127.0.0.1"
        # run
        uvicorn.run(self, **options)

    def gen_starlette_app(self, debug=False, **kwds: Any) -> Any:
        self.simple_starlette_app = Starlette(
            debug=debug,
            routes=self.routes,
            exception_handlers=exception_handlers,
            **kwds
        )
        return self.simple_starlette_app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if not self.simple_starlette_app:
            self.simple_starlette_app = self.gen_starlette_app()
        scope["app"] = self
        await self.simple_starlette_app.middleware_stack(scope, receive, send)

    def __repr__(self) -> str:
        return "<SimpleStarlette '%s'>" % self.app_name
