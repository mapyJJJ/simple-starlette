from typing import Any


class ConfigAttribute(object):
    def __init__(self, attr_name, get_converter: Any = None) -> None:
        self.attr_name = attr_name
        self.get_converter = get_converter

    def __get__(self, obj, type=None):
        print(obj)
        config = getattr(obj, "_config")
        rv = config[self.attr_name]
        if not self.get_converter:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj, value):
        config = getattr(obj, "_config")
        config[self.attr_name] = value
        setattr(obj, "_config", config)
