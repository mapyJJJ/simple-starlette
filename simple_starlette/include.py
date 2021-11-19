# route include
# ~~~~~~~~~~~~~~

import typing
from simple_starlette.app import SimpleStarlette


class IncludeError(Exception):
    Ellipsis


standard_split_flag = ["", "/"]


class Include:
    def __init__(self, app: SimpleStarlette, prefix: str) -> None:
        self.app = app
        (*split_flag, _) = prefix.partition("/")
        if split_flag != standard_split_flag:
            raise IncludeError("prefix cannot format, {}".format(prefix))
        self.prefix = prefix

    def route(self, path: str, **options):
        if not path.startswith("/"):
            path = "/" + path

        def register(cls: typing.Callable):
            methods = []
            for _m in self.app.allow_methods:
                if getattr(cls, _m, None):
                    methods.append(_m.upper())
            self.app.register_route(
                path=self.prefix + path, cls=cls, methods=methods, **options
            )

        return register
