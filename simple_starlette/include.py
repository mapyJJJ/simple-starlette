# route include
# ~~~~~~~~~~~~~~

import typing

from simple_starlette.app import SimpleStarlette


class Include:
    """register route by include

    like flask blueprint

    Usage:

    ```
        from Simple_starlette import SimpleStarlette, Include

        app = SimpleStarlette(__name__)

        api = Include(app, '/api')

        @api.route("/test", allow_methods=["GET])
        async def test(request):
            ...

    ```
    """

    def __init__(self, app: SimpleStarlette, prefix: str) -> None:
        self.app = app
        if not prefix.startswith("/"):
            raise TypeError("prefix must startwith '/'")
        self.prefix = prefix

    def route(self, path: str, websoket_route: bool = False, **options):
        if not path.startswith("/"):
            path = "/" + path

        def register(cls: typing.Callable):
            self.app.route(path, websoket_route=websoket_route, **options)(cls)

        return register
