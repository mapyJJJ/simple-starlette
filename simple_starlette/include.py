from typing import Any
import typing

from starlette.routing import Route


class Include:
    def __init__(self, app, prefix) -> None:
        self.app = app
        self.prefix = prefix

    def route(self, path, **options):
        def register(cls: typing.Callable):
            methods = []
            for _m in self.app.allow_methods:
                if getattr(cls, _m, None):
                    methods.append(_m.upper())
            self.app.routes.append(Route(path, cls, methods=methods))

        return register

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        Ellipsis
