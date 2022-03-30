# json-rpc server, client
# ~~~~~~~~~~~~~~~~~~~~~~~~

import json
import operator
from typing import cast

import requests
from jsonrpcclient import parse, request  # type: ignore
from jsonrpcclient.responses import Ok
from jsonrpcserver import dispatch, method
from jsonrpcserver.result import Success
from starlette.requests import Request
from typing_extensions import Literal

from simple_starlette.app import SimpleStarlette
from simple_starlette.responses import Response, ResTypeEnum


class JsonRpcServer:
    def __init__(self, app: SimpleStarlette) -> None:
        self.app = app
        self.paths = []

    def register_rpc_method(self, path: str = "/", name: str = None):
        def decorator(func):
            self.paths.append(path)
            method(func, name=name)

        return decorator

    def gen_route(self, path):
        async def index(request: Request):
            _d = getattr(request, "data", {})
            return Response(
                dispatch(json.dumps(_d.get("body", {}))),
                ResTypeEnum.JSON,
            )

        self.app.route(path, allow_methods=["POST"])(index)

    def to_response(self, *args):
        return Success(*args)

    def run(
        self,
        host: str = None,
        port: int = None,
        debug: bool = True,
        **options,
    ):
        for _p in self.paths:
            if _p in self.app.get_paths_by_namespace(_p):
                continue
            self.gen_route(_p)
        self.app.run(host=host, port=port, debug=debug, **options)


class JsonRpcClient:
    def __init__(
        self,
        host: str,
        method: Literal["get", "post"] = "post",
        method_name: str = None,
    ) -> None:
        self.host = host
        self.method = method
        self.method_name = method_name

    async def get_response(self, params: dict) -> Ok:
        response = operator.methodcaller(
            self.method.lower(),
            json=request(self.method_name, params=params),
            url=self.host,
        )(requests)
        return cast(Ok, parse(response.json()))
