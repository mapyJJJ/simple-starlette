import asyncio
from simple_starlette import SimpleStarlette, g
import pytest

@pytest.fixture
def app():
    app = SimpleStarlette("test")
    return app

@pytest.fixture
def g():
    return g