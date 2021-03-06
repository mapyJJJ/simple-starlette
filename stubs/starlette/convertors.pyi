import typing
from typing import Any

class Convertor:
    regex: str = ...
    def convert(self, value: str) -> typing.Any: ...
    def to_string(self, value: typing.Any) -> str: ...

class StringConvertor(Convertor):
    regex: str = ...
    def convert(self, value: str) -> typing.Any: ...
    def to_string(self, value: typing.Any) -> str: ...

class PathConvertor(Convertor):
    regex: str = ...
    def convert(self, value: str) -> typing.Any: ...
    def to_string(self, value: typing.Any) -> str: ...

class IntegerConvertor(Convertor):
    regex: str = ...
    def convert(self, value: str) -> typing.Any: ...
    def to_string(self, value: typing.Any) -> str: ...

class FloatConvertor(Convertor):
    regex: str = ...
    def convert(self, value: str) -> typing.Any: ...
    def to_string(self, value: typing.Any) -> str: ...

class UUIDConvertor(Convertor):
    regex: str = ...
    def convert(self, value: str) -> typing.Any: ...
    def to_string(self, value: typing.Any) -> str: ...

CONVERTOR_TYPES: Any
