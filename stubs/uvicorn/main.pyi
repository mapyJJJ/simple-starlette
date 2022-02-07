import click
import typing
from asgiref.typing import ASGIApplication as ASGIApplication
from typing import Any
from uvicorn.config import Config as Config, HTTP_PROTOCOLS as HTTP_PROTOCOLS, INTERFACES as INTERFACES, LIFESPAN as LIFESPAN, LOGGING_CONFIG as LOGGING_CONFIG, LOG_LEVELS as LOG_LEVELS, LOOP_SETUPS as LOOP_SETUPS, SSL_PROTOCOL_VERSION as SSL_PROTOCOL_VERSION, WS_PROTOCOLS as WS_PROTOCOLS
from uvicorn.server import Server as Server, ServerState as ServerState
from uvicorn.supervisors import ChangeReload as ChangeReload, Multiprocess as Multiprocess

LEVEL_CHOICES: Any
HTTP_CHOICES: Any
WS_CHOICES: Any
LIFESPAN_CHOICES: Any
LOOP_CHOICES: Any
INTERFACE_CHOICES: Any
logger: Any

def print_version(ctx: click.Context, param: click.Parameter, value: bool) -> None: ...
def main(app: str, host: str, port: int, uds: str, fd: int, loop: str, http: str, ws: str, ws_max_size: int, ws_ping_interval: float, ws_ping_timeout: float, lifespan: str, interface: str, debug: bool, reload: bool, reload_dirs: typing.List[str], reload_includes: typing.List[str], reload_excludes: typing.List[str], reload_delay: float, workers: int, env_file: str, log_config: str, log_level: str, access_log: bool, proxy_headers: bool, server_header: bool, date_header: bool, forwarded_allow_ips: str, root_path: str, limit_concurrency: int, backlog: int, limit_max_requests: int, timeout_keep_alive: int, ssl_keyfile: str, ssl_certfile: str, ssl_keyfile_password: str, ssl_version: int, ssl_cert_reqs: int, ssl_ca_certs: str, ssl_ciphers: str, headers: typing.List[str], use_colors: bool, app_dir: str, factory: bool) -> None: ...
def run(app: typing.Union[ASGIApplication, str], **kwargs: typing.Any) -> None: ...
