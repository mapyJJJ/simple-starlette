#   request_utils.py
# ~~~~~~~~~~~~~~~~~~~~~

import functools
import inspect
import typing
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from enum import Enum
from typing import Any, Dict, Iterable, Union

from requests.hooks import dispatch_hook
from requests.models import Request, Response
from requests.sessions import PreparedRequest
from requests.sessions import Session as _Session


class HookEvent(str, Enum):
    RESPONSE = "response"
    REQUEST = "request"


class IResponseHook(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, response: Response, **kwds: Any) -> Any:
        Ellipsis


class IRequestHook(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, prepare_req: PreparedRequest, **kwds) -> Any:
        Ellipsis


class Session(_Session):
    """
    Session Class
    """

    def request(
        self,
        method,
        url,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None,
        json=None,
    ):
        request_hooks = []
        if hooks:
            if HookEvent.REQUEST in hooks:
                request_hooks = hooks.pop(HookEvent.REQUEST)
        req = Request(
            method=method.upper(),
            url=url,
            headers=headers,
            files=files,
            data=data or {},
            json=json,
            params=params or {},
            auth=auth,
            cookies=cookies,
            hooks=hooks,
        )
        prep = self.prepare_request(req)

        if request_hooks:
            # handle request hooks
            prep = dispatch_hook(
                HookEvent.REQUEST,
                {HookEvent.REQUEST: request_hooks},
                prep,
            )

        proxies = proxies or {}

        settings = self.merge_environment_settings(
            prep.url, proxies, stream, verify, cert
        )

        send_kwargs = {
            "timeout": timeout,
            "allow_redirects": allow_redirects,
        }
        send_kwargs.update(settings)
        resp = self.send(prep, **send_kwargs)

        return resp


class RequestHookMixin:
    def __init__(self) -> None:
        self._hooks: Dict = defaultdict(list)

    def iter_check_hooks(self, hooks):
        if hasattr(hooks, "__call__"):
            hooks = [hooks]
        for hook in hooks:
            if not inspect.isclass(hook):
                continue
            if issubclass(hook, IResponseHook):
                yield hook
            elif issubclass(hook, IRequestHook):
                yield hook
            continue

    def register_hooks(
        self,
        hook_event: HookEvent,
        hooks: Union[Iterable[typing.Callable], typing.Callable],
    ):
        for valid_hook in self.iter_check_hooks(hooks):
            if valid_hook not in self._hooks[hook_event]:
                self._hooks[hook_event].append(valid_hook)

    def deregister_hooks(
        self,
        hook_event: HookEvent,
        hooks: Union[Iterable[typing.Callable], typing.Callable],
    ):
        if hook_event not in self._hooks:
            return
        event_hooks = []
        for register_hook in self._hooks[hook_event]:
            if register_hook not in self.iter_check_hooks(hooks):
                event_hooks.append(register_hook)
        self._hooks[hook_event] = event_hooks

    @property
    def hooks(self):
        return self._hooks

    @hooks.setter
    def hooks(self, hook_map: dict):
        self._hooks = defaultdict(list)
        for k, v in hook_map.items():
            if not isinstance(v, Iterable):
                v = [v]
            self.register_hooks(k, v)

    @hooks.deleter
    def hooks(self):
        self._hooks = defaultdict(list)


class RequestsCtx:
    def __enter__(self):
        self.session = Session()
        return self

    def __exit__(self, *args: typing.Any):
        del self.session


class Requests(RequestsCtx, RequestHookMixin):
    """
    Requests Class
    """

    def __init__(
        self,
        url=None,
        headers=None,
        proxies=None,
        cookies=None,
        json=None,
        params=None,
        **kwgs: Dict,
    ) -> None:
        self.persist_settions = {
            "url": url,
            "headers": headers,
            "proxies": proxies,
            "cookies": cookies,
            "json": json,
            "params": params,
            **kwgs,
        }
        return super().__init__()

    def request(self, method, url=None, **kwargs):
        _hooks = {}
        for event_key in self.hooks:
            _hooks[event_key] = [_h() for _h in self.hooks[event_key]]
        if not url:
            url = self.persist_settions.get("url") or kwargs.get(
                "url"
            )
        settings = {}
        settings.update(self.persist_settions)
        settings.update(kwargs)
        settings.pop("url", 0)
        request_func = functools.partial(
            self.session.request, method, url
        )
        return request_func(hooks=_hooks, **settings)

    def get(self, url=None, *args, **kwargs) -> Response:
        return self.request("GET", url, *args, **kwargs)

    def post(self, url=None, data=None, json=None, **kwargs):
        return self.request(
            "post", url, data=data, json=json, **kwargs
        )
