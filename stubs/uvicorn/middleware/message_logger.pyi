from asgiref.typing import ASGI3Application as ASGI3Application, ASGIReceiveCallable as ASGIReceiveCallable, ASGIReceiveEvent as ASGIReceiveEvent, ASGISendCallable as ASGISendCallable, ASGISendEvent as ASGISendEvent, WWWScope as WWWScope
from typing import Any
from uvicorn.logging import TRACE_LOG_LEVEL as TRACE_LOG_LEVEL

PLACEHOLDER_FORMAT: Any

def message_with_placeholders(message: Any) -> Any: ...

class MessageLoggerMiddleware:
    task_counter: int = ...
    app: Any = ...
    logger: Any = ...
    def __init__(self, app: ASGI3Application) -> None: ...
    async def __call__(self, scope: WWWScope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...