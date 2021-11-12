from . import base as base
from .. import event as event, exc as exc, util as util
from ..sql import compiler as compiler
from .mock import create_mock_engine as create_mock_engine
from typing import Any

def create_engine(url: Any, **kwargs: Any): ...
def engine_from_config(configuration: Any, prefix: str = ..., **kwargs: Any): ...
