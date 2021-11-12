import typing
from starlette.exceptions import HTTPException as HTTPException
from starlette.requests import HTTPConnection as HTTPConnection, Request as Request
from starlette.responses import RedirectResponse as RedirectResponse, Response as Response
from starlette.websockets import WebSocket as WebSocket
from typing import Any

def has_required_scope(conn: HTTPConnection, scopes: typing.Sequence[str]) -> bool: ...
def requires(scopes: typing.Union[str, typing.Sequence[str]], status_code: int=..., redirect: str=...) -> typing.Callable: ...

class AuthenticationError(Exception): ...

class AuthenticationBackend:
    async def authenticate(self, conn: HTTPConnection) -> typing.Optional[typing.Tuple[AuthCredentials, BaseUser]]: ...

class AuthCredentials:
    scopes: Any = ...
    def __init__(self, scopes: typing.Sequence[str]=...) -> None: ...

class BaseUser:
    @property
    def is_authenticated(self) -> bool: ...
    @property
    def display_name(self) -> str: ...
    @property
    def identity(self) -> str: ...

class SimpleUser(BaseUser):
    username: Any = ...
    def __init__(self, username: str) -> None: ...
    @property
    def is_authenticated(self) -> bool: ...
    @property
    def display_name(self) -> str: ...

class UnauthenticatedUser(BaseUser):
    @property
    def is_authenticated(self) -> bool: ...
    @property
    def display_name(self) -> str: ...
