# db.py
# base on: sqlalchemy
# ~~~~~~~~~~~~~

import asyncio
from typing import TYPE_CHECKING, Any, Generic, Type, TypeVar, cast

from sqlalchemy.ext.asyncio import async_scoped_session, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession as _AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declared_attr
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session


def check_cls_need_tablename(cls):
    if cls.__dict__.get("__abstract__", False) or not any(
        isinstance(b, DeclarativeMeta) for b in cls.__mro__[1:]
    ):
        # 用于被继承的model, 不需要定义tablename
        return False

    for base in cls.__mro__:  # type: ignore
        if "__tablename__" not in base.__dict__:
            continue
        if isinstance(cls.__dict__.get("__tablename__"), declared_attr):
            return False

        return not (
            base is cls
            or base.__dict__.get("__abstract__", False)
            or not isinstance(base, DeclarativeMeta)
        )

    return True


class ModelNameMixin(object):
    """
    tablename use class name
    """

    def __init__(cls, *args, **kwargs):  # type: ignore
        if check_cls_need_tablename(cls):
            cls.__tablename__ = cls.__name__  # type: ignore
        super(ModelNameMixin, cls).__init__(*args, **kwargs)


class BaseModelMeta(ModelNameMixin, DeclarativeMeta):
    Ellipsis


Model = declarative_base(metaclass=BaseModelMeta)


M = TypeVar("M")

if TYPE_CHECKING:

    class DbBaseModel(Generic[M]):
        @staticmethod
        def create(**kwargs) -> M:
            pass


else:

    class DbBaseModel(Generic[M], Model):
        __abstract__ = True

        @classmethod
        def create(cls, **kwargs):
            return cls(**kwargs)


class AsyncSession(_AsyncSession):
    if TYPE_CHECKING:

        def __call__(self, *args: Any, **kwds: Any) -> Session:
            return Session()


class Sqlalchemy:
    def __init__(self, app) -> None:
        self.app = app
        async_session_factory = sessionmaker(
            self.get_engine(), expire_on_commit=False, class_=AsyncSession
        )
        self.Session = cast(
            AsyncSession,
            async_scoped_session(async_session_factory, scopefunc=asyncio.current_task),
        )

    def get_async_session(self):
        return self.Session()

    def get_engine(self):
        SQLALCHEMY_DATABASE_URI = self.app.config.get("SQLALCHEMY_DATABASE_URI", "")
        if not SQLALCHEMY_DATABASE_URI:
            raise AttributeError(
                "use sqlalchemy, the `SQLALCHEMY_DATABASE_URI` must be set"
            )
        if not SQLALCHEMY_DATABASE_URI.startswith("mysql+aiomysql"):
            raise AttributeError("only support `mysql+aiomysql` engine")
        engine = create_async_engine(SQLALCHEMY_DATABASE_URI)
        return engine
