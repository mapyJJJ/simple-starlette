# ctx.py
# ~~~~~~~~~~~~~

import contextvars
from copy import copy, deepcopy
from functools import partial
from types import TracebackType
from typing import (TYPE_CHECKING, Any, Dict, Generic, List, Optional, Type,
                    TypeVar, cast)

from starlette.applications import Receive, Scope, Send, Starlette
from starlette.requests import Request
from werkzeug.local import LocalProxy


class CtxStorage:
    """context var storage"""

    def get(self, name: str, default=None):
        return self.__dict__.get(name, default)

    def pop(self, name: str) -> None:
        if v := self.__dict__.get(name):
            v.pop()
        return

    def set(self, name: str, value: Any):
        if v := self.__dict__.get(name):
            v.append(value)
        else:
            v = [value]
        self.__dict__[name] = v
        return


class LocalVar:
    """contextvars 提供上下文级别的数据隔离"""

    def __init__(self) -> None:
        context_var = contextvars.ContextVar(
            f"LocalVar.storage:{id(self)}"
        )
        self._localvar = context_var

    def set(self, k, v):
        _storage = self._localvar.get(None)
        if not _storage:
            _storage = CtxStorage()
        _storage.set(k, v)
        self._localvar.set(_storage)

    def pop(self, k: str):
        if _storage := self._localvar.get(None):
            _storage.pop(k)
            self._localvar.set(_storage)
        print(
            "popopopop",
            [
                f"{x.__repr__()}:{id(x)}"
                for x in self._localvar.get().get(k)
            ],
        )

    def get(self, name) -> Any:
        if name == "app":
            print("hereherehere")
        return getattr(self._localvar.get(None), name, [None])[-1]


class G(object):
    """使用一个实例对象承载g对象"""

    def __getattribute__(self, __name: str) -> Any:
        return super().__getattribute__(__name)

    def __getattr__(self, name):
        # AttributeError
        return None


class AppCtx:
    """starlette app context var"""

    def __init__(
        self,
        app: Any,
        raise_ctx_exception: bool = False,
    ) -> None:
        self.app = app
        self.g = G()

    def set(self):
        app_ctx_var.set("app", self.app)
        app_ctx_var.set("app.g", self.g)

    def pop(self):
        app_ctx_var.pop("app")
        app_ctx_var.pop("app.g")

    async def __aenter__(self):
        self.set()

    async def __aexit__(
        self,
        type_: Type[Exception],
        value: Exception,
        tb: TracebackType,
    ):
        self.pop()
        if value:
            if value.__traceback__ is not tb:
                raise value.with_traceback(tb)
            else:
                raise value


class RequestCtx:
    """request context var"""

    def __init__(
        self,
        app: Starlette,
        request: Request,
        raise_ctx_exception: bool = False,
    ) -> None:
        self.request = request
        self.app = app

    def set(self):
        app_ctx = AppCtx(self.app)
        app_ctx.set()
        request_ctx_var.set("request", self.request)

    def pop(self):
        request_ctx_var.pop("request")

    async def __aenter__(self):
        self.set()

    async def __aexit__(
        self,
        type_: Type[Exception],
        value: Exception,
        tb: TracebackType,
    ):
        self.pop()

        if value:
            if value.__traceback__ is not tb:
                raise value.with_traceback(tb)
            else:
                raise value


app_ctx_var = LocalVar()
request_ctx_var = LocalVar()

current_app = LocalProxy(partial(app_ctx_var.get, "app"))
g = cast(Any, LocalProxy(partial(app_ctx_var.get, "app.g")))
request = cast(
    Request, LocalProxy(partial(request_ctx_var.get, "request"))
)
