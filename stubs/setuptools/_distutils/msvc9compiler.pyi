import winreg
from distutils.ccompiler import CCompiler
from typing import Any, Optional

RegOpenKeyEx = winreg.OpenKeyEx
RegEnumKey = winreg.EnumKey
RegEnumValue = winreg.EnumValue
RegError: Any
HKEYS: Any
NATIVE_WIN64: Any
VS_BASE: str
WINSDK_BASE: str
NET_BASE: str
PLAT_TO_VCVARS: Any

class Reg:
    def get_value(cls, path: Any, key: Any): ...
    get_value: Any = ...
    def read_keys(cls, base: Any, key: Any): ...
    read_keys: Any = ...
    def read_values(cls, base: Any, key: Any): ...
    read_values: Any = ...
    def convert_mbcs(s: Any): ...
    convert_mbcs: Any = ...

class MacroExpander:
    macros: Any = ...
    vsbase: Any = ...
    def __init__(self, version: Any) -> None: ...
    def set_macro(self, macro: Any, path: Any, key: Any) -> None: ...
    def load_macros(self, version: Any) -> None: ...
    def sub(self, s: Any): ...

def get_build_version(): ...
def normalize_and_reduce_paths(paths: Any): ...
def removeDuplicates(variable: Any): ...
def find_vcvarsall(version: Any): ...
def query_vcvarsall(version: Any, arch: str = ...): ...

VERSION: Any

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
    plat_name: Any = ...
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
    def initialize(self, plat_name: Optional[Any] = ...) -> None: ...
    def object_filenames(self, source_filenames: Any, strip_dir: int = ..., output_dir: str = ...): ...
    def compile(self, sources: Any, output_dir: Optional[Any] = ..., macros: Optional[Any] = ..., include_dirs: Optional[Any] = ..., debug: int = ..., extra_preargs: Optional[Any] = ..., extra_postargs: Optional[Any] = ..., depends: Optional[Any] = ...): ...
    def create_static_lib(self, objects: Any, output_libname: Any, output_dir: Optional[Any] = ..., debug: int = ..., target_lang: Optional[Any] = ...) -> None: ...
    def link(self, target_desc: Any, objects: Any, output_filename: Any, output_dir: Optional[Any] = ..., libraries: Optional[Any] = ..., library_dirs: Optional[Any] = ..., runtime_library_dirs: Optional[Any] = ..., export_symbols: Optional[Any] = ..., debug: int = ..., extra_preargs: Optional[Any] = ..., extra_postargs: Optional[Any] = ..., build_temp: Optional[Any] = ..., target_lang: Optional[Any] = ...) -> None: ...
    def manifest_setup_ldargs(self, output_filename: Any, build_temp: Any, ld_args: Any) -> None: ...
    def manifest_get_embed_info(self, target_desc: Any, ld_args: Any): ...
    def library_dir_option(self, dir: Any): ...
    def runtime_library_dir_option(self, dir: Any) -> None: ...
    def library_option(self, lib: Any): ...
    def find_library_file(self, dirs: Any, lib: Any, debug: int = ...): ...
    def find_exe(self, exe: Any): ...
