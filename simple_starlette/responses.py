# responses
# ~~~~~~~~~~~~

import json
from collections import namedtuple
from enum import Enum
from typing import Any

from starlette.responses import (FileResponse, HTMLResponse, JSONResponse,
                                 PlainTextResponse, RedirectResponse)
from starlette.responses import Response as _Response

ResponseType = namedtuple(
    "responses_type", ["response_type", "response_class"]
)


class ResTypeEnum(Enum):
    JSON = ResponseType("JSON", JSONResponse)
    FILE = ResponseType("FILE", FileResponse)
    HTML = ResponseType("HTML", HTMLResponse)
    TEXT = ResponseType("TEXT", PlainTextResponse)
    REDIRECT = ResponseType("REDIRECT", RedirectResponse)


class Response:
    def __init__(
        self,
        content: Any,
        res_type: ResTypeEnum,
        status_code: int = 200,
        **options,
    ):
        if res_type == ResTypeEnum.JSON:
            if isinstance(content, str):
                res = json.loads(content)
        elif res_type == ResTypeEnum.TEXT:
            res = str(content)
        resp_class = res_type.value.response_class
        options["status_code"] = status_code
        self.resp_instance = resp_class(content=content, **options)

    def __getattr__(self, name: str) -> Any:
        return getattr(self.resp_instance, name)

    def __call__(self, *args, **kwargs):
        return self.resp_instance(*args, **kwargs)
