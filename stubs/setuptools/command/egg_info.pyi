from distutils.filelist import FileList as _FileList
from setuptools import Command as Command, SetuptoolsDeprecationWarning as SetuptoolsDeprecationWarning
from setuptools.command import bdist_egg as bdist_egg
from setuptools.command.sdist import sdist as sdist, walk_revctrl as walk_revctrl
from setuptools.command.setopt import edit_config as edit_config
from setuptools.extern import packaging as packaging
from setuptools.glob import glob as glob
from typing import Any

def translate_pattern(glob: Any): ...

class InfoCommon:
    tag_build: Any = ...
    tag_date: Any = ...
    @property
    def name(self): ...
    def tagged_version(self): ...
    def tags(self): ...
    vtags: Any = ...

class egg_info(InfoCommon, Command):
    description: str = ...
    user_options: Any = ...
    boolean_options: Any = ...
    negative_opt: Any = ...
    egg_base: Any = ...
    egg_name: Any = ...
    egg_info: Any = ...
    egg_version: Any = ...
    broken_egg_info: bool = ...
    def initialize_options(self) -> None: ...
    @property
    def tag_svn_revision(self) -> None: ...
    @tag_svn_revision.setter
    def tag_svn_revision(self, value: Any) -> None: ...
    def save_version_info(self, filename: Any) -> None: ...
    def finalize_options(self) -> None: ...
    def write_or_delete_file(self, what: Any, filename: Any, data: Any, force: bool = ...) -> None: ...
    def write_file(self, what: Any, filename: Any, data: Any) -> None: ...
    def delete_file(self, filename: Any) -> None: ...
    def run(self) -> None: ...
    filelist: Any = ...
    def find_sources(self) -> None: ...
    def check_broken_egg_info(self) -> None: ...

class FileList(_FileList):
    def process_template_line(self, line: Any) -> None: ...
    def include(self, pattern: Any): ...
    def exclude(self, pattern: Any): ...
    def recursive_include(self, dir: Any, pattern: Any): ...
    def recursive_exclude(self, dir: Any, pattern: Any): ...
    def graft(self, dir: Any): ...
    def prune(self, dir: Any): ...
    def global_include(self, pattern: Any): ...
    def global_exclude(self, pattern: Any): ...
    def append(self, item: Any) -> None: ...
    def extend(self, paths: Any) -> None: ...

class manifest_maker(sdist):
    template: str = ...
    use_defaults: int = ...
    prune: int = ...
    manifest_only: int = ...
    force_manifest: int = ...
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    filelist: Any = ...
    def run(self) -> None: ...
    def write_manifest(self) -> None: ...
    def warn(self, msg: Any) -> None: ...
    def add_defaults(self) -> None: ...
    def add_license_files(self) -> None: ...
    def prune_file_list(self) -> None: ...

def write_file(filename: Any, contents: Any) -> None: ...
def write_pkg_info(cmd: Any, basename: Any, filename: Any) -> None: ...
def warn_depends_obsolete(cmd: Any, basename: Any, filename: Any) -> None: ...
def write_requirements(cmd: Any, basename: Any, filename: Any) -> None: ...
def write_setup_requirements(cmd: Any, basename: Any, filename: Any) -> None: ...
def write_toplevel_names(cmd: Any, basename: Any, filename: Any) -> None: ...
def overwrite_arg(cmd: Any, basename: Any, filename: Any) -> None: ...
def write_arg(cmd: Any, basename: Any, filename: Any, force: bool = ...) -> None: ...
def write_entries(cmd: Any, basename: Any, filename: Any) -> None: ...
def get_pkg_info_revision(): ...

class EggInfoDeprecationWarning(SetuptoolsDeprecationWarning): ...
