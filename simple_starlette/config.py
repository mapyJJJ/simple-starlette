# config.py
# ~~~~~~~~~~~~

import json
import os
import types
from typing import Callable


class ConfigAttribute(object):
    def __init__(
        self,
        attr_name,
        get_converter: Callable = None,
        set_check: Callable = None,
    ) -> None:
        self.attr_name = attr_name
        self.set_check = set_check
        self.get_converter = get_converter

    def __get__(self, obj, type=None):
        config = getattr(obj, "_config")
        rv = config[self.attr_name]
        if self.get_converter:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj, value):
        config = getattr(obj, "_config", {})
        if self.set_check:
            value = self.set_check(value)
        config[self.attr_name] = value
        setattr(obj, "_config", config)


class Config(dict):
    """simple starlette config"""

    def from_file(self, file_path: str):
        if file_path.endswith(".py"):
            self.from_pyfile(file_path)
        elif file_path.endswith(".json"):
            self.from_json(file_path)
        else:
            raise TypeError(
                "Other types of files are not currently supported, only supported pyfile, jsonfile"
            )

    def from_pyfile(self, pyfile_path: str):
        # 从py文件导入配置
        if not os.path.exists(pyfile_path):
            raise OSError(
                "config pyfile {} not exists !".format(
                    str(pyfile_path)
                )
            )
        d = types.ModuleType("config")
        d.__file__ = pyfile_path
        try:
            with open(pyfile_path, "rb") as pyfile:
                r = pyfile.read()
                exec(compile(r, pyfile_path, "exec"), d.__dict__)
        except IOError as e:
            e.strerror = (
                "Unable to load configuration file {}".format(
                    e.strerror
                )
            )
            raise
        self._from_obj(d)
        return

    def from_json(self, jsonfile_path: str):
        # 从json文件导入配置
        if not os.path.exists(jsonfile_path):
            raise OSError(
                "config pyfile {} on exists !".format(
                    str(jsonfile_path)
                )
            )
        try:
            with open(jsonfile_path) as jsonfile:
                d = json.loads(jsonfile.read())
        except IOError as e:
            e.strerror = (
                "Unable to load configuration file {}".format(
                    e.strerror
                )
            )
            raise
        self._from_mappings(d)

    def _from_mappings(self, mappings):
        for _k, _v in mappings.items():
            if _k.isupper():
                self[_k] = _v
        return

    def _from_obj(self, obj):
        for k in dir(obj):
            if k.isupper():
                self[k] = getattr(obj, k)
        return
