from setuptools.extern.packaging.specifiers import SpecifierSet as SpecifierSet
from setuptools.extern.packaging.version import InvalidVersion as InvalidVersion, Version as Version
from typing import Any, Optional

class StaticModule:
    def __init__(self, name: Any) -> None: ...
    def __getattr__(self, attr: Any): ...

def patch_path(path: Any) -> None: ...
def read_configuration(filepath: Any, find_others: bool = ..., ignore_option_errors: bool = ...): ...
def configuration_to_dict(handlers: Any): ...
def parse_configuration(distribution: Any, command_options: Any, ignore_option_errors: bool = ...): ...

class ConfigHandler:
    section_prefix: Any = ...
    aliases: Any = ...
    ignore_option_errors: Any = ...
    target_obj: Any = ...
    sections: Any = ...
    set_options: Any = ...
    def __init__(self, target_obj: Any, options: Any, ignore_option_errors: bool = ...) -> None: ...
    @property
    def parsers(self) -> None: ...
    def __setitem__(self, option_name: Any, value: Any) -> None: ...
    def parse_section(self, section_options: Any) -> None: ...
    def parse(self) -> None: ...

class ConfigMetadataHandler(ConfigHandler):
    section_prefix: str = ...
    aliases: Any = ...
    strict_mode: bool = ...
    package_dir: Any = ...
    def __init__(self, target_obj: Any, options: Any, ignore_option_errors: bool = ..., package_dir: Optional[Any] = ...) -> None: ...
    @property
    def parsers(self): ...

class ConfigOptionsHandler(ConfigHandler):
    section_prefix: str = ...
    @property
    def parsers(self): ...
    def parse_section_packages__find(self, section_options: Any): ...
    def parse_section_entry_points(self, section_options: Any) -> None: ...
    def parse_section_package_data(self, section_options: Any) -> None: ...
    def parse_section_exclude_package_data(self, section_options: Any) -> None: ...
    def parse_section_extras_require(self, section_options: Any) -> None: ...
    def parse_section_data_files(self, section_options: Any) -> None: ...