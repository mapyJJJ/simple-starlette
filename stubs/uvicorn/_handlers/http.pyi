import asyncio
from uvicorn.config import Config as Config
from uvicorn.server import ServerState as ServerState

async def handle_http(reader: asyncio.StreamReader, writer: asyncio.StreamWriter, server_state: ServerState, config: Config) -> None: ...
