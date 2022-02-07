import jinja2
import typing
from os import PathLike
from starlette.background import BackgroundTask as BackgroundTask
from starlette.responses import Response as Response
from starlette.types import Receive as Receive, Scope as Scope, Send as Send
from typing import Any

pass_context: Any

class _TemplateResponse(Response):
    media_type: str = ...
    template: Any = ...
    context: Any = ...
    def __init__(self, template: typing.Any, context: dict, status_code: int=..., headers: dict=..., media_type: str=..., background: BackgroundTask=...) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...

class Jinja2Templates:
    env: Any = ...
    def __init__(self, directory: typing.Union[str, PathLike]) -> None: ...
    def get_template(self, name: str) -> jinja2.Template: ...
    def TemplateResponse(self, name: str, context: dict, status_code: int=..., headers: dict=..., media_type: str=..., background: BackgroundTask=...) -> _TemplateResponse: ...
