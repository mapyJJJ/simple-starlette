from contextvars import ContextVar, copy_context

from werkzeug.local import LocalProxy

global_var = ContextVar("global_var")


class CtxStorage:
    def get(self, name: str, default=None):
        return self.__dict__.get(name, default)

    def pop(self, name: str, default=None):
        if default:
            self.__dict__.pop(name, default)
        else:
            self.__dict__.pop(name)
        return


def get_global_var():
    if global_var not in copy_context():
        global_var.set(CtxStorage())
    return global_var.get()


g = LocalProxy(get_global_var)
