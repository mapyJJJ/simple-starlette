from setuptools.command.egg_info import write_requirements as write_requirements
from setuptools.extern.packaging.tags import sys_tags as sys_tags
from setuptools.extern.packaging.utils import canonicalize_name as canonicalize_name
from typing import Any

WHEEL_NAME: Any
NAMESPACE_PACKAGE_INIT: str

def unpack(src_dir: Any, dst_dir: Any) -> None: ...

class Wheel:
    filename: Any = ...
    def __init__(self, filename: Any) -> None: ...
    def tags(self): ...
    def is_compatible(self): ...
    def egg_name(self): ...
    def get_dist_info(self, zf: Any): ...
    def install_as_egg(self, destination_eggdir: Any) -> None: ...
