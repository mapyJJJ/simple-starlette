# db.py
# base on: sqlalchemy
# asyncio orm docs: https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html
# ~~~~~~~~~~~~~

import functools
import re
from typing import TYPE_CHECKING, Any, Dict, Generic, TypeVar

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import async_scoped_session, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession as _AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declared_attr
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import Session

from simple_starlette.ctx import g


def check_cls_need_tablename(cls):
    if cls.__dict__.get("__abstract__", False) or not any(
        isinstance(b, DeclarativeMeta) for b in cls.__mro__[1:]
    ):
        return False

    for base in cls.__mro__:  # type: ignore
        if "__tablename__" not in base.__dict__:
            continue
        if isinstance(
            cls.__dict__.get("__tablename__"), declared_attr
        ):
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
            # 当没有主动定义 __tablename__ 时，默认取class name作为表名，如果是驼峰则转为snake
            name = cls.__name__  # type: ignore
            if "_" in name:
                cls.__tablename__ = name
            else:
                cls.__tablename__ = name[0].lower() + re.sub(
                    r"([A-Z])",
                    lambda res: "_" + res.groups()[0].lower(),
                    name[1:],
                )

            cls.__tablename__ = cls.__name__.lower()  # type: ignore
        super(ModelNameMixin, cls).__init__(*args, **kwargs)


class BaseModelMeta(ModelNameMixin, DeclarativeMeta):
    Ellipsis


M = TypeVar("M")


class DbBaseModel(
    Generic[M], declarative_base(metaclass=BaseModelMeta)
):
    __abstract__ = True

    if TYPE_CHECKING:

        @classmethod
        def create(cls, **kwargs) -> M:
            ...

    else:

        @classmethod
        def create(cls, **kwargs):
            return cls(**kwargs)


class AsyncSession(_AsyncSession):
    if TYPE_CHECKING:

        def __call__(self, *args: Any, **kwds: Any) -> Session:
            return Session()


class Sqlalchemy:
    """
    init sqlalchemy
    """

    DB_POOL_SIZE: int = 30

    DB_POOL_RECYCLE: int = 7200

    DB_POOL_MAX_OVERFLOW: int = 0

    DB_URIS: Dict[str, str] = {"master": "sqlite:///memory:"}

    def __init__(self, app, async_io=True, **kwargs) -> None:
        """
        app -- simple-starlette app 实例
        async_io -- 使用异步io操作数据库
        """
        self.async_io = async_io
        config_options = self.make_configs(app, kwargs)
        self.create_engine_func = (
            create_async_engine if async_io else create_engine
        )
        self.engine_map = self.create_engine(config_options)
        self.sessionmaker = functools.partial(
            sessionmaker,
            expire_on_commit=False,
            class_=AsyncSession if async_io else Session,
        )
        self.session_factory_map = {}

    def make_configs(self, app, options):
        options.setdefault(
            "db_uris", app.config.get("DB_URIS") or self.DB_URIS
        )
        options.setdefault(
            "pool_size",
            app.config.get("DB_POOL_SIZE") or self.DB_POOL_SIZE,
        )
        options.setdefault(
            "pool_recycle",
            app.config.get("DB_POOL_RECYCLE") or self.DB_POOL_RECYCLE,
        )
        options.setdefault(
            "max_overflow",
            app.config.get("DB_POOL_MAX_OVERFLOW")
            or self.DB_POOL_MAX_OVERFLOW,
        )
        return options

    def create_engine(self, options: dict):
        uri_map: Dict[str, str] = options.pop("db_uris")
        engine_map = {}

        def _engine_create(uri_name):
            engine_map[uri_name] = self.create_engine_func(
                uri_map[uri_name], **options
            )

        for _u in uri_map:
            _engine_create(_u)

        return engine_map

    @staticmethod
    def gen_scopefunc(session_name: str):
        def scopefunc():
            from asyncio import current_task

            return f"{current_task()}_{session_name}"

        return scopefunc

    def set_ctx_db(self, name: str):
        """set default db on context
        db = Sqlalchemy(app)
        db.set_ctx_db("db_master")

        session = db.session()

        ...
        """

        if name not in self.engine_map:
            raise ValueError(
                f"db_name {name} not found, please check `db_uri` config"
            )
        g.__ctx_db_name = name

    def session(self, name: str = None):
        """
        db = Sqlalchemy(app)

        session = db.session("master_db")

        ...

        """
        name = name or g.get("__ctx_db_name", None)
        if _session := self.session_factory_map.get(name):
            return _session()

        _session_factory = self.sessionmaker(
            bind=self.engine_map[name]
        )
        _session = (
            async_scoped_session(
                _session_factory, scopefunc=self.gen_scopefunc(name)
            )
            if self.async_io
            else scoped_session(
                _session_factory, scopefunc=self.gen_scopefunc(name)
            )
        )
        self.session_factory_map[name] = _session
        return _session()
