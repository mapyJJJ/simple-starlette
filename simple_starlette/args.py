# args.py
# ~~~~~~~~

import pydantic

from simple_starlette.types import ArgsT

register_args_models = {}


class BaseModel(pydantic.BaseModel):
    Ellipsis


def register_args(cls: ArgsT) -> ArgsT:
    cls_name = getattr(cls, "__name__")
    if not issubclass(cls, BaseModel):  # type: ignore
        raise TypeError(
            "registed obj must be a simple_starlette.args.BaseModel subclass, {}".format(
                cls_name
            )
        )
    if cls_name in register_args_models:
        raise AttributeError("{} aleary in register models".format(cls_name))
    register_args_models[cls_name] = cls
    return cls
