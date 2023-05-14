# args.py
# ~~~~~~~~

from abc import ABCMeta
from typing import Callable, Dict, Optional, Union, cast, overload

import pydantic

from simple_starlette.types import ArgsT


class BaseModel(pydantic.BaseModel, metaclass=ABCMeta):
    ...


class QueryParams(BaseModel, metaclass=ABCMeta):
    ...


class BodyParams(BaseModel, metaclass=ABCMeta):
    ...


class ResponseParams(BaseModel, metaclass=ABCMeta):
    ...


request_args_model_map: Dict[str, Union[QueryParams, BodyParams]] = {}



@overload
def register_args(cls: ArgsT) -> ArgsT:
    ...

@overload
def register_args() -> Callable:
    ...
    
def register_args(cls: Optional[ArgsT] = None) -> Union[Callable, ArgsT]:    
    if not cls:
        return lambda cls: register_args(cls)  # type: ignore

    cls_name = getattr(cls, "__name__")
    if issubclass(cls, (QueryParams, BodyParams)):  # type: ignore
        if cls_name in request_args_model_map:
            raise AttributeError(
                "{} aleary in register models".format(cls_name)
            )
        request_args_model_map[cls_name] = cls
    else:
        raise Exception(
            "define args class must be subclass of QueryParams or BodyParams"
        )
    return cls  # type: ignore
