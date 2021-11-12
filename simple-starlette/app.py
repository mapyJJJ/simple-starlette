import typing
from typing import Any
from starlette.routing import Route
from starlette.applications import Starlette


class SimpleStarlette:
    # all route
    routes = []

    # allow http method
    allow_methods = ["GET", "POST"]

    def __init__(self, app_name: str) -> None:
        self.app_name = app_name

    def route(self, path, **options):
        def register(cls: typing.Callable):
            methods = []
            for _m in self.allow_methods:
                if getattr(cls, _m, None):
                    methods.append(_m.upper())
            self.routes.append(Route(path, cls, methods=methods))

        return register

    def gen_app(self, debug=False, **kwds: Any) -> Any:
        self.simple_starlette_app = Starlette(routes=self.routes, debug=debug, **kwds)
        return self.simple_starlette_app

    def __repr__(self) -> str:
        return "<SimpleStarlette '%s'>" % self.app_name
