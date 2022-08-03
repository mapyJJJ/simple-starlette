import typing

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


def CorsMiddlewareGenFunc(
    allow_origins: typing.Sequence[str] = (),
    allow_methods: typing.Sequence[str] = ("GET",),
    allow_headers: typing.Sequence[str] = (),
    allow_credentials: bool = False,
    allow_origin_regex: str = None,
    expose_headers: typing.Sequence[str] = (),
    max_age: int = 600,
):
    options = {}
    options["max_age"] = max_age
    options["allow_origins"] = allow_origins
    options["allow_methods"] = allow_methods
    options["allow_headers"] = allow_headers
    options["expose_headers"] = expose_headers
    options["allow_credentials"] = allow_credentials
    options["allow_origin_regex"] = allow_origin_regex
    return Middleware(CORSMiddleware, **options)
