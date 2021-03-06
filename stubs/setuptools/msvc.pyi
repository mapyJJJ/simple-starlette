from .monkey import get_unpatched as get_unpatched
from setuptools.extern.more_itertools import unique_everseen as unique_everseen
from setuptools.extern.packaging.version import LegacyVersion as LegacyVersion
from typing import Any, Optional

class winreg:
    HKEY_USERS: Any = ...
    HKEY_CURRENT_USER: Any = ...
    HKEY_LOCAL_MACHINE: Any = ...
    HKEY_CLASSES_ROOT: Any = ...

def msvc9_find_vcvarsall(version: Any): ...
def msvc9_query_vcvarsall(ver: Any, arch: str = ..., *args: Any, **kwargs: Any): ...

PLAT_SPEC_TO_RUNTIME: Any

def msvc14_get_vc_env(plat_spec: Any): ...
def msvc14_gen_lib_options(*args: Any, **kwargs: Any): ...

class PlatformInfo:
    current_cpu: Any = ...
    arch: Any = ...
    def __init__(self, arch: Any) -> None: ...
    @property
    def target_cpu(self): ...
    def target_is_x86(self): ...
    def current_is_x86(self): ...
    def current_dir(self, hidex86: bool = ..., x64: bool = ...): ...
    def target_dir(self, hidex86: bool = ..., x64: bool = ...): ...
    def cross_dir(self, forcex86: bool = ...): ...

class RegistryInfo:
    HKEYS: Any = ...
    pi: Any = ...
    def __init__(self, platform_info: Any) -> None: ...
    @property
    def visualstudio(self): ...
    @property
    def sxs(self): ...
    @property
    def vc(self): ...
    @property
    def vs(self): ...
    @property
    def vc_for_python(self): ...
    @property
    def microsoft_sdk(self): ...
    @property
    def windows_sdk(self): ...
    @property
    def netfx_sdk(self): ...
    @property
    def windows_kits_roots(self): ...
    def microsoft(self, key: Any, x86: bool = ...): ...
    def lookup(self, key: Any, name: Any): ...

class SystemInfo:
    WinDir: Any = ...
    ProgramFiles: Any = ...
    ProgramFilesx86: Any = ...
    ri: Any = ...
    pi: Any = ...
    known_vs_paths: Any = ...
    vs_ver: Any = ...
    def __init__(self, registry_info: Any, vc_ver: Optional[Any] = ...) -> None: ...
    def find_reg_vs_vers(self): ...
    def find_programdata_vs_vers(self): ...
    @property
    def VSInstallDir(self): ...
    @property
    def VCInstallDir(self): ...
    @property
    def WindowsSdkVersion(self): ...
    @property
    def WindowsSdkLastVersion(self): ...
    @property
    def WindowsSdkDir(self): ...
    @property
    def WindowsSDKExecutablePath(self): ...
    @property
    def FSharpInstallDir(self): ...
    @property
    def UniversalCRTSdkDir(self): ...
    @property
    def UniversalCRTSdkLastVersion(self): ...
    @property
    def NetFxSdkVersion(self): ...
    @property
    def NetFxSdkDir(self): ...
    @property
    def FrameworkDir32(self): ...
    @property
    def FrameworkDir64(self): ...
    @property
    def FrameworkVersion32(self): ...
    @property
    def FrameworkVersion64(self): ...

class EnvironmentInfo:
    pi: Any = ...
    ri: Any = ...
    si: Any = ...
    def __init__(self, arch: Any, vc_ver: Optional[Any] = ..., vc_min_ver: int = ...) -> None: ...
    @property
    def vs_ver(self): ...
    @property
    def vc_ver(self): ...
    @property
    def VSTools(self): ...
    @property
    def VCIncludes(self): ...
    @property
    def VCLibraries(self): ...
    @property
    def VCStoreRefs(self): ...
    @property
    def VCTools(self): ...
    @property
    def OSLibraries(self): ...
    @property
    def OSIncludes(self): ...
    @property
    def OSLibpath(self): ...
    @property
    def SdkTools(self): ...
    @property
    def SdkSetup(self): ...
    @property
    def FxTools(self): ...
    @property
    def NetFxSDKLibraries(self): ...
    @property
    def NetFxSDKIncludes(self): ...
    @property
    def VsTDb(self): ...
    @property
    def MSBuild(self): ...
    @property
    def HTMLHelpWorkshop(self): ...
    @property
    def UCRTLibraries(self): ...
    @property
    def UCRTIncludes(self): ...
    @property
    def FSharp(self): ...
    @property
    def VCRuntimeRedist(self): ...
    def return_env(self, exists: bool = ...): ...
