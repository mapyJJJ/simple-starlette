from setuptools.command.setopt import config_file as config_file, edit_config as edit_config, option_base as option_base
from typing import Any

def shquote(arg: Any): ...

class alias(option_base):
    description: str = ...
    command_consumes_arguments: bool = ...
    user_options: Any = ...
    boolean_options: Any = ...
    args: Any = ...
    remove: Any = ...
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...

def format_alias(name: Any, aliases: Any): ...
