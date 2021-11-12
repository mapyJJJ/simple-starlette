import typing as t

class CommonRequestDescriptorsMixin:
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...

class CommonResponseDescriptorsMixin:
    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None: ...
