"""
This type stub file was generated by pyright.
"""

import asyncio
from typing import Any, Callable

HEADER_RE: Any
HEADER_VALUE_RE: Any
STATUS_LINE: Any
class HttpToolsProtocol(asyncio.Protocol):
    config: Any = ...
    app: Any = ...
    on_connection_lost: Any = ...
    loop: Any = ...
    logger: Any = ...
    access_logger: Any = ...
    access_log: Any = ...
    parser: Any = ...
    ws_protocol_class: Any = ...
    root_path: Any = ...
    limit_concurrency: Any = ...
    timeout_keep_alive_task: Any = ...
    timeout_keep_alive: Any = ...
    server_state: Any = ...
    connections: Any = ...
    tasks: Any = ...
    default_headers: Any = ...
    transport: Any = ...
    flow: Any = ...
    server: Any = ...
    client: Any = ...
    scheme: Any = ...
    pipeline: Any = ...
    url: Any = ...
    scope: Any = ...
    headers: Any = ...
    expect_100_continue: bool = ...
    cycle: Any = ...
    def __init__(self, config: Any, server_state: Any, on_connection_lost: Callable = ..., _loop: Any = ...) -> None:
        ...
    
    def connection_made(self, transport: Any) -> None:
        ...
    
    def connection_lost(self, exc: Any) -> None:
        ...
    
    def eof_received(self) -> None:
        ...
    
    def data_received(self, data: Any) -> None:
        ...
    
    def handle_upgrade(self) -> None:
        ...
    
    def on_url(self, url: Any) -> None:
        ...
    
    def on_header(self, name: bytes, value: bytes) -> Any:
        ...
    
    def on_headers_complete(self) -> None:
        ...
    
    def on_body(self, body: bytes) -> Any:
        ...
    
    def on_message_complete(self) -> None:
        ...
    
    def on_response_complete(self) -> None:
        ...
    
    def shutdown(self) -> None:
        ...
    
    def pause_writing(self) -> None:
        ...
    
    def resume_writing(self) -> None:
        ...
    
    def timeout_keep_alive_handler(self) -> None:
        ...
    


class RequestResponseCycle:
    scope: Any = ...
    transport: Any = ...
    flow: Any = ...
    logger: Any = ...
    access_logger: Any = ...
    access_log: Any = ...
    default_headers: Any = ...
    message_event: Any = ...
    on_response: Any = ...
    disconnected: bool = ...
    keep_alive: Any = ...
    waiting_for_100_continue: Any = ...
    body: bytes = ...
    more_body: bool = ...
    response_started: bool = ...
    response_complete: bool = ...
    chunked_encoding: Any = ...
    expected_content_length: int = ...
    def __init__(self, scope: Any, transport: Any, flow: Any, logger: Any, access_logger: Any, access_log: Any, default_headers: Any, message_event: Any, expect_100_continue: Any, keep_alive: Any, on_response: Any) -> None:
        ...
    
    async def run_asgi(self, app: Any) -> None:
        ...
    
    async def send_500_response(self) -> None:
        ...
    
    async def send(self, message: Any) -> None:
        ...
    
    async def receive(self):
        ...
    


