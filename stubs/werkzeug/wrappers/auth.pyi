import typing as t

class AuthorizationMixin:
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...

class WWWAuthenticateMixin:
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
