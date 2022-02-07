from distutils.errors import *
from distutils.cmd import Command as Command
from distutils.config import PyPIRCCommand as PyPIRCCommand
from distutils.extension import Extension as Extension
from typing import Any, Optional

USAGE: str

def gen_usage(script_name: Any): ...

setup_keywords: Any
extension_keywords: Any

def setup(**attrs: Any): ...
def run_commands(dist: Any): ...
def run_setup(script_name: Any, script_args: Optional[Any] = ..., stop_after: str = ...): ...
