import functools
import inspect
import re
import os.path
from collections import defaultdict
from dataclasses import MISSING, dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import pydantic
import pydantic.fields
from pydantic.main import ModelMetaclass
from starlette.requests import Request
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from simple_starlette.args import (BodyParams, QueryParams, ResponseParams,
                                   request_args_model_map)
from simple_starlette.cache.memory_cache import local_g
from simple_starlette.responses import Response, ResTypeEnum
from simple_starlette.route import Route

methods = ("GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS", "PATCH")


def snake_to_camel(ori: str):
    ori = ori.capitalize()
    ori = re.sub(r"_(\S)", lambda g: g.groups()[0].capitalize(), ori)
    return ori


def register_api(
    app,
    target_func: Callable,
    version: str = "v1",
    allow_methods: List[str] = ["GET"],
):
    app.route(
        path=f"/docs-api/{version}/{target_func.__name__}",
        allow_methods=allow_methods,
        name=snake_to_camel(target_func.__name__),
        include_in_schema=False,
    )(target_func)


@dataclass
class ArgDocs:
    name: str
    required: bool
    default: str
    arg_type: str
    description: str


@dataclass
class apiDocsItem:
    path: str
    include: str
    method: str
    describe: str
    querys: List[ArgDocs]
    bodys: List[ArgDocs]
    responses: List[ArgDocs]
    data_model_map: Dict[str, Any]


def extract_data_model(
    field: pydantic.fields.ModelField,
) -> List[ModelMetaclass]:
    models = []
    field_type = field.type_
    if isinstance(field_type, ModelMetaclass):
        arg_tuple = (field_type,)
    else:
        arg_tuple = field.type_.__dict__.get("__args__", ())

    def for_each_arg_tuple(arg_tuple: Tuple[Any]):
        for arg in arg_tuple:
            if str(type(arg)) == "type":
                # 基础类型
                continue
            elif isinstance(arg, ModelMetaclass):
                # basemodel
                models.append(arg)
            elif "typing" in str(type(arg)):
                # 解析seq
                for_each_arg_tuple(arg.__dict__["__args__"])
            else:
                continue

    for_each_arg_tuple(arg_tuple)
    return models


def parse_args_docs(
    cls, view_func: Callable
) -> Tuple[Dict[str, list], List[ModelMetaclass]]:
    def _match_arg_model(name: str):
        return request_args_model_map.get(name, None)

    base_models = []
    args_dict = defaultdict(list)
    for _, t in list(view_func.__annotations__.items())[1:]:
        _args_model_name = t.__name__
        args_model = t
        if not args_model:
            continue
        arg_docs_list = []
        for _fn, _field in args_model.__fields__.items():
            arg_type = _field._type_display()
            sub_base_models = extract_data_model(_field)
            base_models.extend(sub_base_models)
            arg_type = arg_type.replace("typing.", "")
            for _m in sub_base_models:
                arg_type = re.sub(
                    f"__main__.*{_m.__name__}", _m.__name__, arg_type
                )
            arg_type = re.sub(
                r"<class '(.*)'>",
                lambda res: res.groups()[0],
                arg_type,
            )

            arg_docs_list.append(
                ArgDocs(
                    name=_fn,
                    arg_type=arg_type.replace("typing.", ""),
                    default=_field.default,
                    required=_field.required,
                    description=_field.field_info.description,
                ).__dict__
            )
        if issubclass(args_model, QueryParams):
            _key = "query_args"
        elif issubclass(args_model, BodyParams):
            _key = "body_args"
        elif issubclass(args_model, ResponseParams):
            _key = "response_args"
        else:
            continue
        args_dict[_key].extend(arg_docs_list)
    return args_dict, base_models


def parse_route_for_docs(route: Route) -> List[apiDocsItem]:
    endpoint = route.endpoint
    include_name = route.include_name or "other"
    view_funcs: List[Tuple[list, Callable]] = []
    api_docs_list = []
    if inspect.isfunction(endpoint):
        view_funcs.append((route.methods, endpoint))
    else:
        for _method in route.methods:
            if _view_func := getattr(endpoint, _method.lower(), None):
                view_funcs.append(([_method.lower()], _view_func))
    for methods, view_func in view_funcs:
        args_dict, base_models = parse_args_docs(endpoint, view_func)
        data_model_map = {}
        for base_model in base_models:
            _base_model_dict = {}
            for (k, v) in base_model.__annotations__.items():
                _base_model_dict[k] = getattr(
                    v, "__qualname__", "any"
                )
            data_model_map[base_model.__name__] = _base_model_dict
        api_docs_list.extend(
            [
                apiDocsItem(
                    path=route.path,
                    method=method.upper(),
                    include=include_name,
                    data_model_map=data_model_map,
                    querys=args_dict.get("query_args", []),
                    bodys=args_dict.get("body_args", []),
                    describe=(view_func.__doc__ or "").strip(),
                    responses=args_dict.get("response_args", []),
                ).__dict__
                for method in methods
            ]
        )
    return api_docs_list


class DocsApi:
    """
    docs api for simpleApiDocs
    Look github:
    """

    @staticmethod
    async def ping(request: Request):
        return Response("ok", ResTypeEnum.TEXT)

    @staticmethod
    async def api_list(request: Request):
        path_route_map = local_g["routes"]
        _res = []
        for _, route in path_route_map.items():
            if not getattr(route, "include_in_schema", None):
                continue

            api_docs_list = parse_route_for_docs(route=route)
            _res.extend(api_docs_list)
        return Response({"api_docs_list": _res}, ResTypeEnum.JSON)

    @staticmethod
    async def index(request: Request):
        fn = open(
            "simple_starlette/docs/react_static/index.html", "r"
        )
        return Response(fn, ResTypeEnum.HTML)

    def __init__(self, app) -> None:
        _register_api = functools.partial(
            register_api, app=app, version="v1"
        )
        _register_api(target_func=self.ping, allow_methods=["GET"])
        _register_api(
            target_func=self.api_list, allow_methods=["GET"]
        )
        directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), "react_static")
        app.routes["/"] = Mount(
            "/docs",
            app=StaticFiles(
                directory=directory
            ),
            name="docs",
        )
