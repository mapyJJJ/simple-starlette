import typing as t

class CORSRequestMixin:
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...

class CORSResponseMixin:
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
