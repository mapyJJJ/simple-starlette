# args.py
# ~~~~~~~~

from abc import ABCMeta

import pydantic

from simple_starlette.types import ArgsT

register_args_models = {}


class BaseModel(pydantic.BaseModel, metaclass=ABCMeta):
    Ellipsis


class QueryParams(BaseModel, metaclass=ABCMeta):
    Ellipsis


class BodyParams(BaseModel, metaclass=ABCMeta):
    Ellipsis


class ResponseParams(BaseModel, metaclass=ABCMeta):
    Ellipsis


def register_args(cls: ArgsT) -> ArgsT:
    cls_name = getattr(cls, "__name__")
    if issubclass(cls, (QueryParams, BodyParams)):  # type: ignore
        if cls_name in register_args_models:
            raise AttributeError(
                "{} aleary in register models".format(cls_name)
            )
        register_args_models[cls_name] = cls
    else:
        raise Exception(
            "define args class must be subclass of QueryParams or BodyParams"
        )
    return cls  # type: ignore
