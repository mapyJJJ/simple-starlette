from starlette.requests import Request as Request
from starlette.responses import Response as Response, StreamingResponse as StreamingResponse
from starlette.types import ASGIApp as ASGIApp, Receive as Receive, Scope as Scope, Send as Send
from typing import Any

RequestResponseEndpoint: Any
DispatchFunction: Any

class BaseHTTPMiddleware:
    app: Any = ...
    dispatch_func: Any = ...
    def __init__(self, app: ASGIApp, dispatch: DispatchFunction=...) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response: ...
