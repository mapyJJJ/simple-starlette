from setuptools import Command as Command, namespaces as namespaces
from setuptools.archive_util import unpack_archive as unpack_archive
from typing import Any

class install_egg_info(namespaces.Installer, Command):
    description: str = ...
    user_options: Any = ...
    install_dir: Any = ...
    def initialize_options(self) -> None: ...
    source: Any = ...
    target: Any = ...
    outputs: Any = ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_outputs(self): ...
    def copytree(self): ...
