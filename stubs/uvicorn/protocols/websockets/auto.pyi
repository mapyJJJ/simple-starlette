import asyncio
import typing
from uvicorn.protocols.websockets.websockets_impl import WebSocketProtocol as WebSocketProtocol
from uvicorn.protocols.websockets.wsproto_impl import WSProtocol as WSProtocol

AutoWebSocketsProtocol: typing.Optional[typing.Type[asyncio.Protocol]]
AutoWebSocketsProtocol = WSProtocol
AutoWebSocketsProtocol = WebSocketProtocol
