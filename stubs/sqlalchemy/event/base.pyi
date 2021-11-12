from .. import util as util
from typing import Any, Optional

class _UnpickleDispatch:
    def __call__(self, _instance_cls: Any): ...

class _Dispatch:
    def __init__(self, parent: Any, instance_cls: Optional[Any] = ...) -> None: ...
    def __getattr__(self, name: Any): ...
    def __reduce__(self): ...

class _EventMeta(type):
    def __init__(cls, classname: Any, bases: Any, dict_: Any) -> None: ...

class Events: ...

class _JoinedDispatcher:
    local: Any = ...
    parent: Any = ...
    def __init__(self, local: Any, parent: Any) -> None: ...
    def __getattr__(self, name: Any): ...

class dispatcher:
    dispatch: Any = ...
    events: Any = ...
    def __init__(self, events: Any) -> None: ...
    def __get__(self, obj: Any, cls: Any): ...

class slots_dispatcher(dispatcher):
    def __get__(self, obj: Any, cls: Any): ...
