import distutils.command.build_clib as orig
from setuptools.dep_util import newer_pairwise_group as newer_pairwise_group
from typing import Any

class build_clib(orig.build_clib):
    def build_libraries(self, libraries: Any) -> None: ...
