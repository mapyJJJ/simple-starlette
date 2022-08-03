# dispatch request
# ~~~~~~~~~~~~~~~~~

import asyncio
import functools
import inspect
import typing
from inspect import isfunction
from typing import Callable

import pydantic
from starlette.requests import Request

from simple_starlette.args import (BodyParams, QueryParams, ResponseParams,
                                   register_args_models)

from .exceptions import RequestArgsNoMatch

try:
    # python3.6 +
    import contextvars
except:
    contextvars = None


def find_view_func(obj: typing.Any, method: str):
    if not obj:
        raise Exception(404)
    if inspect.isfunction(obj):
        return obj
    return getattr(obj(), method.lower(), None)


def is_coroutine(obj: typing.Any) -> bool:
    while isinstance(obj, functools.partial):
        obj = obj.func
    return inspect.iscoroutinefunction(obj)


async def run_in_eventloop(func: typing.Callable, *args, **kwargs):
    """
    first create event loop
    if has context, run in context
    """
    loop = asyncio.get_event_loop()
    if contextvars:
        child_func = functools.partial(func, *args, **kwargs)
        context = contextvars.copy_context()
        func = context.run
        args = (child_func,)
    elif kwargs:
        func = functools.partial(func, **kwargs)
    return await loop.run_in_executor(None, func, *args)


async def introduce_dependant_args(
    cls, func: typing.Any, data: typing.Mapping, request: Request
):
    """introduce depends"""

    def _match_arg_model(name: str):
        return register_args_models.get(name, None)

    kwargs = {}
    for k, t in list(func.__annotations__.items())[1:]:
        # _args_model_name = t.__name__
        # if isfunction(cls):
        #     args_model = _match_arg_model(_args_model_name)
        # else:
        #     args_model = getattr(
        #         cls,
        #         _args_model_name,
        #         _match_arg_model(_args_model_name),
        #     )
        args_model = t
        if args_model is None:
            raise Exception("no define arg obj")

        try:
            if issubclass(args_model, QueryParams):
                kwargs[k] = args_model.parse_obj(
                    data.get("query") or {}
                )
            elif issubclass(args_model, BodyParams):
                if request.method.upper() == "POST":
                    kwargs[k] = args_model.parse_obj(
                        data.get("body") or {}
                    )
                else:
                    kwargs[k] = None
            elif issubclass(args_model, ResponseParams):
                kwargs[k] = None
        except Exception as e:
            raise RequestArgsNoMatch(err_msg=str(e), err_code=4041)
    return kwargs


async def dispatch_request(
    cls,
    request: Request,
    data: typing.Mapping[
        typing.Literal["query", "body"], typing.Dict
    ],
):
    """dispatch request
    register all views obj in routes
    find target func and return response
    """
    view_func = typing.cast(
        Callable, find_view_func(cls, request.method)
    )

    # 针对没有使用async await关键定义的视图函数，进行统一处理
    is_coroutine_func = is_coroutine(view_func)

    # 根据当前request.ctx 获取相关信息，导入视图所需依赖
    kwargs = (
        await introduce_dependant_args(cls, view_func, data, request)
        or {}
    )

    if is_coroutine_func:
        # 可被await的func，自动运行在eventloop中
        response = await view_func(request, **kwargs)
    else:
        # 如果函数不具备await，则新创建事件循环，并在其中运行
        response = await run_in_eventloop(
            view_func, request, **kwargs
        )
    return response
