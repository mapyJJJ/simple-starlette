# ctx.py
# ~~~~~~~~~~~~~

import contextvars
from typing import TYPE_CHECKING, Any

from werkzeug.local import LocalProxy

global_var = contextvars.ContextVar("global_var")


class CtxStorage:
    """ctx storage class"""

    def get(self, name: str, default=None):
        return self.__dict__.get(name, default)

    def pop(self, name: str, default=None):
        if default:
            self.__dict__.pop(name, default)
        else:
            self.__dict__.pop(name)
        return


def get_global_var():
    """get current ctx var"""

    if global_var in contextvars.copy_context():
        return global_var.get()
    else:
        global_var.set(CtxStorage())
    return global_var.get()


if TYPE_CHECKING:

    class G:
        def __getattribute__(self, name: str) -> Any:
            pass

        def __setattr__(self, __name: str, __value):
            pass

    g = G()
else:
    g = LocalProxy(get_global_var)
