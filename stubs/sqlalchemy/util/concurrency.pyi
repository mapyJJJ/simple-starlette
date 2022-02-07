from . import compat as compat
from ._compat_py3k import asynccontextmanager as asynccontextmanager
from ._concurrency_py3k import AsyncAdaptedLock as AsyncAdaptedLock, asyncio as asyncio, await_fallback as await_fallback, await_only as await_only, greenlet_spawn as greenlet_spawn, is_exit_exception as is_exit_exception

have_greenlet: bool
