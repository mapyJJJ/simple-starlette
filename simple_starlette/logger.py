import logging
from typing import Optional

import click

__all__ = ["getLogger"]


def getLogger(
    namespace: str,
    formatter_str: str = "",
    level=logging.DEBUG,
    log_file_path: Optional[str] = None,
):
    logger = logging.getLogger(namespace)
    handler = logging.StreamHandler()
    file_handle = None
    if log_file_path:
        file_handle = logging.FileHandler(log_file_path)

    prefix_formatter_str = click.style(
        "%(levelname)s:" + " " * 5, "green"
    )
    formatter_str = prefix_formatter_str + (
        formatter_str or "%(message)s"
    )
    formatter = logging.Formatter(formatter_str)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if file_handle:
        logger.addHandler(file_handle)
    logger.setLevel(level)
    return logger
