import typing
from uvicorn.supervisors.basereload import BaseReload
from uvicorn.supervisors.multiprocess import Multiprocess as Multiprocess

ChangeReload: typing.Type[BaseReload]
