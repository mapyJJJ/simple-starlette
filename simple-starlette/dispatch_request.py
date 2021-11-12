import typing
import inspect
import asyncio
import pydantic
import functools

from starlette.requests import Request

try:
    # python3.6 +
    import contextvars
except:
    contextvars = None


def find_func(cls: typing.Any, method: str):
    func = getattr(cls(), method.lower(), None)
    if not func:
        raise Exception(404)
    return func


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
        kwargs[_key] = _arg_obj(**data)
        if not issubclass(_arg_obj, pydantic.BaseModel):
            raise Exception("_arg_obj must be pydantic.BaseModel")

    if is_coroutine_func:
        # execute view func
        response = await func(request, **kwargs)
    else:
        # run view func on threadpool
        response = await run_in_threadpool(func, request)
    return response
