"""
This type stub file was generated by pyright.
"""

import itertools
import operator
from collections import namedtuple
from datetime import tzinfo
from functools import reduce
from typing import Any, Optional

py39: Any
py38: Any
py37: Any
py3k: Any
py2k: Any
pypy: Any
cpython: Any
win32: Any
osx: Any
arm: Any
has_refcount_gc: Any
contextmanager = ...
dottedgetter = operator.attrgetter
namedtuple = ...
next = ...
FullArgSpec = ...
class nullcontext:
    enter_result: Any = ...
    def __init__(self, enter_result: Optional[Any] = ...) -> None:
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, *excinfo: Any) -> None:
        ...
    


def inspect_getfullargspec(func: Any):
    ...

def importlib_metadata_get(group: Any):
    ...

string_types: Any
binary_types: Any
binary_type = ...
text_type = ...
int_types: Any
iterbytes = ...
long_type = ...
itertools_filterfalse = itertools.filterfalse
itertools_filter = filter
itertools_imap = map
exec_: Any
import_: Any
print_: Any
def b(s: Any):
    ...

def b64decode(x: Any):
    ...

def b64encode(x: Any):
    ...

def decode_backslashreplace(text: Any, encoding: Any):
    ...

def cmp(a: Any, b: Any):
    ...

def raise_(exception: Any, with_traceback: Optional[Any] = ..., replace_context: Optional[Any] = ..., from_: bool = ...) -> None:
    ...

def u(s: Any):
    ...

def ue(s: Any):
    ...

callable = ...
class ABC:
    __metaclass__: Any = ...


binary_type = ...
text_type = ...
long_type = ...
callable = ...
cmp = ...
reduce = ...
b64encode = ...
b64decode = ...
def safe_bytestring(text: Any):
    ...

def inspect_formatargspec(args: Any, varargs: Optional[Any] = ..., varkw: Optional[Any] = ..., defaults: Optional[Any] = ..., kwonlyargs: Any = ..., kwonlydefaults: Any = ..., annotations: Any = ..., formatarg: Any = ..., formatvarargs: Any = ..., formatvarkw: Any = ..., formatvalue: Any = ..., formatreturns: Any = ..., formatannotation: Any = ...):
    ...

def dataclass_fields(cls):
    ...

def local_dataclass_fields(cls):
    ...

def raise_from_cause(exception: Any, exc_info: Optional[Any] = ...) -> None:
    ...

def reraise(tp: Any, value: Any, tb: Optional[Any] = ..., cause: Optional[Any] = ...) -> None:
    ...

def with_metaclass(meta: Any, *bases: Any, **kw: Any):
    ...

class timezone(tzinfo):
    def __init__(self, offset: Any) -> None:
        ...
    
    def __eq__(self, other: Any) -> Any:
        ...
    
    def __hash__(self) -> Any:
        ...
    
    def utcoffset(self, dt: Any):
        ...
    
    def tzname(self, dt: Any):
        ...
    
    def dst(self, dt: Any) -> None:
        ...
    
    def fromutc(self, dt: Any):
        ...
    


