# route include
# ~~~~~~~~~~~~~~

from typing import Callable, List

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
        self.prefix = prefix[:-1] if prefix.endswith("/") else prefix

    def route(
        self,
        path: str,
        allow_methods: List[str] = [],
        websocket_route: bool = False,
        **options,
    ):
        if not path.startswith("/"):
            path = "/" + path

        options["include_name"] = self.prefix

        def register(cls: Callable):
            self.app.route(
                path=self.prefix + path,
                websocket_route=websocket_route,
                allow_methods=allow_methods,
                **options,
            )(cls)

        return register
