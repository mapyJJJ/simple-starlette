from typing import Generic, TypeVar

from sqlalchemy.sql.selectable import Select as _Select


class Select(_Select):
    def __init__(self, *args, **kwargs) -> None:
        ...