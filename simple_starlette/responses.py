from typing import Any
from enum import Enum
from starlette.responses import (
    JSONResponse,
    PlainTextResponse,
    FileResponse,
    HTMLResponse,
    RedirectResponse,
)
from collections import namedtuple

ResponseType = namedtuple("responses_type", ["response_type", "response_class"])


class ResTypeEnum(Enum):
    JSON = ResponseType("JSON", JSONResponse)
    FILE = ResponseType("FILE", FileResponse)
    HTML = ResponseType("HTML", HTMLResponse)
    TEXT = ResponseType("TEXT", PlainTextResponse)
    REDIRECT = ResponseType("REDIRECT", RedirectResponse)


class Response:
    def __init__(self, res: Any, res_type: ResTypeEnum, **options) -> Any:
        self.res = res
        self.res_class = res_type.value.response_class

    async def __call__(self, *args: Any, **kwds: Any) -> Any:
        await self.res_class(content=self.res).__call__(*args, **kwds)
