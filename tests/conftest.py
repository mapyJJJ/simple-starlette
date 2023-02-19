import pytest
from simple_starlette import SimpleStarlette, g

@pytest.fixture
def app():
    app = SimpleStarlette("test")
    return app

@pytest.fixture
def g():
    return g