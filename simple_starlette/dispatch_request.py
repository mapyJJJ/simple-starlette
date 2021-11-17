import asyncio
import functools
import inspect
import typing

import pydantic
from starlette.requests import Request

from .exceptions import RequestArgsNoMatch

try:
    # python3.6 +
    import contextvars
except:
    contextvars = None


def find_func(obj: typing.Any, method: str):
    if not obj:
        raise Exception(404)
    if not inspect.isfunction(obj):
        obj = getattr(obj(), method.lower(), None)
    return obj


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


async def dispatch_request(cls, request: Request, data: typing.Mapping):
    # dispatch request
    # register all views obj in routes
    # find target func and return response
    func = find_func(cls, request.method)

    # check func iscoroutine
    is_coroutine_func = is_coroutine(func)

    # Introduce dependent parameters to the view function
    # use pydantic check request args and body
    kwargs = {}
    for _key, _type in func.__annotations__.items():
        _arg_obj_name = _type.__name__
        if _arg_obj_name in ("Request"):
            continue
        _arg_obj = getattr(cls, _arg_obj_name, None)
        if not _arg_obj:
            raise Exception("no define obj")
        if not issubclass(_arg_obj, pydantic.BaseModel):
            raise Exception("_arg_obj must be pydantic.BaseModel")
        try:
            kwargs[_key] = _arg_obj.parse_obj(data)
        except pydantic.ValidationError as e:
            raise RequestArgsNoMatch(msg=e.errors(), status_code=4041)

    if is_coroutine_func:
        # execute view func
        response = await func(request, **kwargs)
    else:
        # run view func on threadpool
        response = await run_in_threadpool(func, request, **kwargs)
    return response
