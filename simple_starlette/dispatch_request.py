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

from simple_starlette.args import register_args_models

from .exceptions import RequestArgsNoMatch

try:
    # python3.6 +
    import contextvars
except:
    contextvars = None


def find_func(obj: typing.Any, method: str):
    # 兼容fbv, cbv
    if not obj:
        raise Exception(404)
    if inspect.isfunction(obj):
        return obj
    return getattr(obj(), method.lower(), None)


def is_coroutine(obj: typing.Any) -> bool:
    while isinstance(obj, functools.partial):
        obj = obj.func
    return inspect.iscoroutinefunction(obj)


async def run_in_threadpool(func: typing.Callable, *args, **kwargs):
    # create event loop
    loop = asyncio.get_event_loop()
    if contextvars:
        child_func = functools.partial(func, *args, **kwargs)
        context = contextvars.copy_context()
        # execute on lifespan
        func = context.run
        args = (child_func,)
    elif kwargs:
        func = functools.partial(func, **kwargs)
    # use default executor
    return await loop.run_in_executor(None, func, *args)


async def introduce_dependant_args(cls, func: Callable, data: typing.Mapping):
    kwargs = {}
    for k, t in func.__annotations__.items():
        _args_model_name = t.__name__
        if _args_model_name in ("Request"):
            continue

        _args_model_obj = None
        if not isfunction(cls):
            _args_model_obj = getattr(cls, _args_model_name, None)
        else:
            _args_model_obj = register_args_models.get(_args_model_name, None)

        if _args_model_obj is None:
            raise Exception("no define arg obj")

        try:
            kwargs[k] = _args_model_obj.parse_obj(data)
        except pydantic.ValidationError as e:
            raise RequestArgsNoMatch(err_msg=e.errors(), status_code=4041)
        return kwargs


async def dispatch_request(cls, request: Request, data: typing.Mapping):
    # dispatch request
    # register all views obj in routes
    # find target func and return response
    func = find_func(cls, request.method)

    # check func iscoroutine
    is_coroutine_func = is_coroutine(func)

    # Introduce dependent parameters to the view function
    # use pydantic check request args and body
    kwargs = await introduce_dependant_args(cls, func, data) or {}

    if is_coroutine_func:
        # execute view func
        response = await func(request, **kwargs)
    else:
        # run view func on threadpool
        response = await run_in_threadpool(func, request, **kwargs)
    return response
