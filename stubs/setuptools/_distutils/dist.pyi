from distutils.errors import *
from typing import Any, Optional

command_re: Any

class Distribution:
    global_options: Any = ...
    common_usage: str = ...
    display_options: Any = ...
    display_option_names: Any = ...
    negative_opt: Any = ...
    verbose: int = ...
    dry_run: int = ...
    help: int = ...
    metadata: Any = ...
    cmdclass: Any = ...
    command_packages: Any = ...
    script_name: Any = ...
    script_args: Any = ...
    command_options: Any = ...
    dist_files: Any = ...
    packages: Any = ...
    package_data: Any = ...
    package_dir: Any = ...
    py_modules: Any = ...
    libraries: Any = ...
    headers: Any = ...
    ext_modules: Any = ...
    ext_package: Any = ...
    include_dirs: Any = ...
    extra_path: Any = ...
    scripts: Any = ...
    data_files: Any = ...
    password: str = ...
    command_obj: Any = ...
    have_run: Any = ...
    want_user_cfg: bool = ...
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...
    def get_option_dict(self, command: Any): ...
    def dump_option_dicts(self, header: Optional[Any] = ..., commands: Optional[Any] = ..., indent: str = ...) -> None: ...
    def find_config_files(self): ...
    def parse_config_files(self, filenames: Optional[Any] = ...) -> None: ...
    commands: Any = ...
    def parse_command_line(self): ...
    def finalize_options(self) -> None: ...
    def handle_display_options(self, option_order: Any): ...
    def print_command_list(self, commands: Any, header: Any, max_length: Any) -> None: ...
    def print_commands(self) -> None: ...
    def get_command_list(self): ...
    def get_command_packages(self): ...
    def get_command_class(self, command: Any): ...
    def get_command_obj(self, command: Any, create: int = ...): ...
    def reinitialize_command(self, command: Any, reinit_subcommands: int = ...): ...
    def announce(self, msg: Any, level: Any = ...) -> None: ...
    def run_commands(self) -> None: ...
    def run_command(self, command: Any) -> None: ...
    def has_pure_modules(self): ...
    def has_ext_modules(self): ...
    def has_c_libraries(self): ...
    def has_modules(self): ...
    def has_headers(self): ...
    def has_scripts(self): ...
    def has_data_files(self): ...
    def is_pure(self): ...

class DistributionMetadata:
    name: Any = ...
    version: Any = ...
    author: Any = ...
    author_email: Any = ...
    maintainer: Any = ...
    maintainer_email: Any = ...
    url: Any = ...
    license: Any = ...
    description: Any = ...
    long_description: Any = ...
    keywords: Any = ...
    platforms: Any = ...
    classifiers: Any = ...
    download_url: Any = ...
    provides: Any = ...
    requires: Any = ...
    obsoletes: Any = ...
    def __init__(self, path: Optional[Any] = ...) -> None: ...
    def read_pkg_file(self, file: Any): ...
    def write_pkg_info(self, base_dir: Any) -> None: ...
    def write_pkg_file(self, file: Any) -> None: ...
    def get_name(self): ...
    def get_version(self): ...
    def get_fullname(self): ...
    def get_author(self): ...
    def get_author_email(self): ...
    def get_maintainer(self): ...
    def get_maintainer_email(self): ...
    def get_contact(self): ...
    def get_contact_email(self): ...
    def get_url(self): ...
    def get_license(self): ...
    get_licence: Any = ...
    def get_description(self): ...
    def get_long_description(self): ...
    def get_keywords(self): ...
    def set_keywords(self, value: Any) -> None: ...
    def get_platforms(self): ...
    def set_platforms(self, value: Any) -> None: ...
    def get_classifiers(self): ...
    def set_classifiers(self, value: Any) -> None: ...
    def get_download_url(self): ...
    def get_requires(self): ...
    def set_requires(self, value: Any) -> None: ...
    def get_provides(self): ...
    def set_provides(self, value: Any) -> None: ...
    def get_obsoletes(self): ...
    def set_obsoletes(self, value: Any) -> None: ...

def fix_help_options(options: Any): ...