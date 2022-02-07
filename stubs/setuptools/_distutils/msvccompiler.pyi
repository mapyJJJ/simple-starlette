import win32con
import winreg
from distutils.ccompiler import CCompiler
from distutils.msvc9compiler import MSVCCompiler
from typing import Any, Optional

hkey_mod = winreg
RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError: Any
hkey_mod = win32con
HKEYS: Any

def read_keys(base: Any, key: Any): ...
def read_values(base: Any, key: Any): ...
def convert_mbcs(s: Any): ...

class MacroExpander:
    macros: Any = ...
    def __init__(self, version: Any) -> None: ...
    def set_macro(self, macro: Any, path: Any, key: Any) -> None: ...
    def load_macros(self, version: Any) -> None: ...
    def sub(self, s: Any): ...

def get_build_version(): ...
def get_build_architecture(): ...
def normalize_and_reduce_paths(paths: Any): ...

class MSVCCompiler(CCompiler):
    compiler_type: str = ...
    executables: Any = ...
    src_extensions: Any = ...
    res_extension: str = ...
    obj_extension: str = ...
    static_lib_extension: str = ...
    shared_lib_extension: str = ...
    static_lib_format: str = ...
    shared_lib_format: str = ...
    exe_extension: str = ...
    initialized: bool = ...
    def __init__(self, verbose: int = ..., dry_run: int = ..., force: int = ...) -> None: ...
    cc: str = ...
    linker: str = ...
    lib: str = ...
    rc: str = ...
    mc: str = ...
    preprocess_options: Any = ...
    compile_options: Any = ...
    compile_options_debug: Any = ...
    ldflags_shared: Any = ...
    ldflags_shared_debug: Any = ...
    ldflags_static: Any = ...
    def initialize(self) -> None: ...
    def object_filenames(self, source_filenames: Any, strip_dir: int = ..., output_dir: str = ...): ...
    def compile(self, sources: Any, output_dir: Optional[Any] = ..., macros: Optional[Any] = ..., include_dirs: Optional[Any] = ..., debug: int = ..., extra_preargs: Optional[Any] = ..., extra_postargs: Optional[Any] = ..., depends: Optional[Any] = ...): ...
    def create_static_lib(self, objects: Any, output_libname: Any, output_dir: Optional[Any] = ..., debug: int = ..., target_lang: Optional[Any] = ...) -> None: ...
    def link(self, target_desc: Any, objects: Any, output_filename: Any, output_dir: Optional[Any] = ..., libraries: Optional[Any] = ..., library_dirs: Optional[Any] = ..., runtime_library_dirs: Optional[Any] = ..., export_symbols: Optional[Any] = ..., debug: int = ..., extra_preargs: Optional[Any] = ..., extra_postargs: Optional[Any] = ..., build_temp: Optional[Any] = ..., target_lang: Optional[Any] = ...) -> None: ...
    def library_dir_option(self, dir: Any): ...
    def runtime_library_dir_option(self, dir: Any) -> None: ...
    def library_option(self, lib: Any): ...
    def find_library_file(self, dirs: Any, lib: Any, debug: int = ...): ...
    def find_exe(self, exe: Any): ...
    def get_msvc_paths(self, path: Any, platform: str = ...): ...
    def set_path_env_var(self, name: Any) -> None: ...
OldMSVCCompiler = MSVCCompiler