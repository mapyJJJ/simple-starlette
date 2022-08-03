import logging

import click
from uvicorn.config import LOGGING_CONFIG


def change_uvicorn_access_fmt():
    LOGGING_CONFIG["formatters"]["access"][
        "fmt"
    ] = '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'


uvicorn_logger_map = {
    logging.INFO: lambda name, message: logging.getLogger(
        "uvicorn.error"
    ).warn(f'{click.style(name, fg="green")}:{" "*5}{message}')
}

change_uvicorn_access_fmt()
