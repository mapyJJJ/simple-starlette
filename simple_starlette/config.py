# config.py
# ~~~~~~~~~~~~

import json
import os
import types
from typing import Any


class ConfigAttribute(object):
    def __init__(self, attr_name, get_converter: Any = None) -> None:
        self.attr_name = attr_name
        self.get_converter = get_converter

    def __get__(self, obj, type=None):
        config = getattr(obj, "_config")
        rv = config[self.attr_name]
        if not self.get_converter:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj, value):
        config = getattr(obj, "_config")
        config[self.attr_name] = value
        setattr(obj, "_config", config)


class Config(dict):
    """simple starlette config"""

    def from_pyfile(self, pyfile_path: str):
        if not os.path.exists(pyfile_path):
            raise OSError("config pyfile {} on exists !".format(str(pyfile_path)))
        d = types.ModuleType("config")
        d.__file__ = pyfile_path
        try:
            with open(pyfile_path, "rb") as pyfile:
                r = pyfile.read()
                exec(compile(r, pyfile_path, "exec"), d.__dict__)
        except IOError as e:
            e.strerror = "Unable to load configuration file {}".format(e.strerror)
            raise
        self.from_obj(d)
        return

    def from_json(self, jsonfile_path: str):
        if not os.path.exists(jsonfile_path):
            raise OSError("config pyfile {} on exists !".format(str(jsonfile_path)))
        try:
            with open(jsonfile_path) as jsonfile:
                d = json.loads(jsonfile.read())
        except IOError as e:
            e.strerror = "Unable to load configuration file {}".format(e.strerror)
            raise
        self.from_mappings(d)

    def from_mappings(self, mappings):
        for _k, _v in mappings.items():
            if _k.isupper():
                self[_k] = _v
        return

    def from_obj(self, obj):
        for k in dir(obj):
            if k.isupper():
                self[k] = getattr(obj, k)
        return
