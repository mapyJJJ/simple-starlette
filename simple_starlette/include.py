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

    def route(self, path: str, websoket_route: bool = False, **options):
        if not path.startswith("/"):
            path = "/" + path

        def register(cls: typing.Callable):
            self.app.route(path, websoket_route=websoket_route, **options)(cls)

        return register
