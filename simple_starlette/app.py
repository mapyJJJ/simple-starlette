#   app.py
# ~~~~~~~~~~~

import inspect
import typing
import warnings
from textwrap import dedent
from typing import Callable, Dict, List, Literal, NewType, cast

import uvicorn
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp, Receive, Scope, Send
from starlette.websockets import WebSocket

from simple_starlette.cache.memory_cache import local_g
from simple_starlette.config import Config, ConfigAttribute
from simple_starlette.ctx import AppCtx
from simple_starlette.docs.api import DocsApi
from simple_starlette.types import Route as _RouteT

from .exceptions import exception_handlers
from .logger import getLogger
from .middleware.rate_limiter import RateLimiterMiddleWare
from .route import Route, WebSocketRoute
from .types import _L_M

logger = getLogger(__name__)
_ASGIAPP = NewType("_ASGIAPP", ASGIApp)
_Receive = NewType("_Receive", Receive)
_Send = NewType("_Send", Send)
_Scope = NewType("_Scope", Scope)

class AllowMethodsAttrConverter:
    @staticmethod
    def _make_methods_right(v):
        if not isinstance(v, list):
            raise TypeError("attr `allow_methods` must be list value")
        if all(isinstance(n, str) for n in v):
            v = list(map(lambda e: e.lower(), v))
            return v
        raise TypeError("`method` must be string type")


class SimpleStarlette:
    """
    SimpleStarlette base on Starlette
    Did some more friendly to developers of functional adaptation
    simple_starlette are designed to facilitate quick used to create Web Project
    """

    run_env: Literal["prod", "dev"] = "prod"

    config_class = Config

    routes: Dict[str, Route] = {}

    allow_default_methods = ConfigAttribute(
        "allow_default_methods",
        set_check=AllowMethodsAttrConverter._make_methods_right,
    )

    simple_starlette_app: Starlette

    websocket_routes: Dict[str, WebSocketRoute] = {}

    def echo_framework_name(self):
        print(
            dedent(
                """
   _____ _                 __    _____ __             __     __  __
  / ___/(_)___ ___  ____  / /__ / ___// /_____ ______/ /__  / /_/ /____
  \__ \/ / __ `__ \/ __ \/ / _ \\__ \/ __/ __ `/ ___/ / _ \/ __/ __/ _ \\
 ___/ / / / / / / / /_/ / /  __/__/ / /_/ /_/ / /  / /  __/ /_/ /_/  __/
/____/_/_/ /_/ /_/ .___/_/\___/____/\__/\__,_/_/  /_/\___/\__/\__/\___/
                /_/
                """
            )
        )
        return

    def __init__(
        self,
        app_name: str,
        config_path: typing.Optional[str] = None,
        allow_methods: List[str] = [],
        run_env: Literal["prod", "dev"] = "prod",
        middleware: _L_M = None,
        after_request_stack: typing.Optional[
            typing.List[Callable]
        ] = None,
        before_reqeuest_stack: typing.Optional[
            typing.List[Callable]
        ] = None,
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
        :config_path
            read config file, load in env
        :allow_methods
            allow register router http methods, default [get, post]
        :run_env
        :middleware
            starlette middleware, look startlette.middlewares/
        :after_request_stack
            do something after request handle complete
        :before_reqeuest_stack
            do something before receive request

        """
        self.app_name = app_name
        self.run_env = run_env

        self.allow_default_methods = allow_methods or [
            "get",
            "post",
            "put",
            "delete",
            "patch",
            "options",
        ]

        self.config = self.make_config(config_path)
        self.middleware = middleware or []

        # convert request hook to middleware
        self.after_request_stack = (
            after_request_stack if after_request_stack else []
        )

        self.before_request_stack = (
            before_reqeuest_stack if before_reqeuest_stack else []
        )

        # echo framework name ascii name
        self.echo_framework_name()

    def preflight_check_middleware_order(
        self, user_middleware: _L_M = None
    ):
        """
        TIPS:
            这是一个尴尬的问题，在cors验证前做一些cookie相关的工作，会导致程序混乱
            理论上 cors中间件完全应该作为第一个中间件进行处理
        """
        if not user_middleware:
            return []
        middleware_priority = {
            CORSMiddleware: "0",
            RateLimiterMiddleWare: "1",
        }
        user_middleware.sort(
            key=lambda x: middleware_priority.get(x.cls, 9999)
        )
        for _m in user_middleware:
            logger.info("已加载中间件: %s" % (_m.cls.__name__))
        return user_middleware

    def route(
        self,
        path: str,
        allow_methods: List[str] = [],
        websocket_route: bool = False,
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

        def CheckViewFuncParamsDefinition(
            view_func: Callable, websocket_route: bool
        ):
            right_obj = WebSocket if websocket_route else Request

            if not view_func.__annotations__:
                raise Exception(
                    f"视图函数: {view_func.__name__} 没有接收任何参数"
                )

            first_param_type = list(
                view_func.__annotations__.items()
            )[0][1]
            assert (
                first_param_type is right_obj
            ), f"""
                The first parameter must be used to receive the {right_obj.__name__} object, for example:

                    from simple_starlette import SimpleStarlette
                    from simple_starlette import Request
                    
                    app = SimpleStarlette(__name__)

                    @app.route("/one", allow_methods=["GET"])
                    async def admin_one(request: Request):  # <-- like this !!!
                        return Response("ok", ResTypeEnum.TEXT)
            """

        def register(cls: typing.Callable) -> _RouteT:
            if websocket_route:
                assert (
                    path not in self.websocket_routes
                ), f"same path `{path}` has been register"
                route = WebSocketRoute(path, cls, **options)
                self.websocket_routes[path] = route
            if inspect.isfunction(cls) or inspect.iscoroutinefunction(
                cls
            ):
                CheckViewFuncParamsDefinition(cls, websocket_route)

                if not websocket_route and not allow_methods:
                    raise Exception(
                        f"if websocket request, the allow_methods do not need to be set, in the `{path}` around"
                    )

                route = Route(
                    path, cls, methods=allow_methods, **options
                )
                self.routes[path] = route

            else:
                if allow_methods:
                    warnings.warn(
                        "endpoint is class, params: allow_methods is useless"
                    )
                methods = []
                for _m in allow_methods or self.allow_default_methods:
                    if view_func := getattr(cls, _m.lower(), None):
                        CheckViewFuncParamsDefinition(
                            view_func, websocket_route
                        )
                        methods.append(_m.upper())
                if not methods:
                    raise Exception(
                        "not found any http method func in endpoint, {}".format(
                            cls.__class__.__name__
                        )
                    )
                route = Route(path, cls, methods=methods, **options)
                self.routes[path] = route
            return typing.cast(_RouteT, route)

        return register

    def run(
        self,
        host: typing.Optional[str] = None,
        port: typing.Optional[int] = None,
        debug: bool = False,
        reload: bool = False,
        workers: typing.Optional[int] = None,
        limit_concurrency: typing.Optional[int] = None,
        limit_max_requests: typing.Optional[int] = None,
        timeout_keep_alive: int = 5,
        **options,
    ):
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
        options["debug"] = debug
        options["reload"] = reload
        options["workers"] = workers
        options["limit_concurrency"] = limit_concurrency
        options["limit_max_requests"] = limit_max_requests
        options["timeout_keep_alive"] = timeout_keep_alive

        options["port"] = port or self.config.get("PORT", 9091)
        options["host"] = host or self.config.get("HOST", "127.0.0.1")

        port = self.config["PORT"] = options["port"]
        host = self.config["HOST"] = options["host"]

        if self.run_env == "dev":
            local_g["routes"] = self.routes
            DocsApi(self)
            logger.info(f"api文档加载:")
            logger.info(
                f"api文档地址: http://{host}:{port}/docs/index.html"
            )
        logger.info(f"运行环境:{self.run_env}")
        uvicorn.run(cast(_ASGIAPP, self), **options)

    def rquest_hook(self, starlette_app):
        """use starlette http middleware"""

        if self.before_request_stack or self.after_request_stack:

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

        if starlette_app := getattr(self, "starlette_app", None):
            return starlette_app

        starlette_app = Starlette(
            middleware=self.preflight_check_middleware_order(
                user_middleware=self.middleware
            ),
            exception_handlers=exception_handlers,
            debug=self.config.get("DEBUG", False),
            routes=list([r for r in self.iter_all_routes()]),
        )
        self.rquest_hook(starlette_app)
        self.starlette_app = starlette_app
        return starlette_app

    def load_conf_from_file(self, config_path: str) -> None:
        self.config.from_file(config_path)

    def make_config(self, config_path: typing.Optional[str] = None):
        """return config object"""
        default_config = {
            "DEBUG": False,
            "ENV": None,
            "HOST": "localhost",
            "PORT": 9091,
        }
        conf = self.config_class(default_config)
        if config_path:
            conf.from_file(config_path)
        return conf

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

    async def __call__(
        self, scope: _Scope, receive: _Receive, send: _Send
    ) -> None:
        scope["app"] = self
        starlette_app = self.gen_starlette_app()
        # middleware_stack 确保 error_handler中间件在最外，以便捕获全局errors
        await starlette_app.middleware_stack(scope, receive, send)

    def context_app(self, raise_ctx_exception: bool = False):
        """
        from simple_starlette import SimpleStarlette

        app = SimpleStarlette(__name__)

        with app.context_app():
            db = sqlalchemy_db_init()
            db.query(User).filter()....
        """

        return AppCtx(self, raise_ctx_exception)

    def __repr__(self) -> str:
        return "<SimpleStarlette '%s'>" % self.app_name
