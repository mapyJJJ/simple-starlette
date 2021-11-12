import typing as t
from .wrappers.request import Request as Request
from .wrappers.response import Response as Response
from _typeshed.wsgi import StartResponse, WSGIEnvironment as WSGIEnvironment
from typing import Any

logo: Any
TEMPLATE: str

def iter_sys_path() -> t.Iterator[t.Tuple[str, bool, bool]]: ...
def render_testapp(req: Request) -> bytes: ...
def test_app(environ: WSGIEnvironment, start_response: StartResponse) -> t.Iterable[bytes]: ...
