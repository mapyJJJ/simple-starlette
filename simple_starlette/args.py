__all__ = ["register_args_models", "register_args"]

from typing import TypeVar

import pydantic

register_args_models = {}


class BaseArgsError(Exception):
    Ellipsis


T = TypeVar("T", bound=object)


class BaseModel(pydantic.BaseModel):
    Ellipsis


def register_args(cls: T) -> T:
    cls_name = getattr(cls, "__name__")
    if not issubclass(cls, BaseModel):  # type: ignore
        raise BaseArgsError(
            "registed obj must be a simple_starlette.args.BaseModel subclass, {}".format(
                cls_name
            )
        )
    if cls_name in register_args_models:
        raise BaseArgsError("{} aleary in register models".format(cls_name))
    register_args_models[cls_name] = cls
    return cls
