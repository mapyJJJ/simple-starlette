# db.py
# base on: sqlalchemy
# base on sqlalchemy 1.4 , use  async io
# asyncio orm docs: https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html
# ~~~~~~~~~~~~~

import logging
import random
import re
from datetime import datetime
from typing import (TYPE_CHECKING, Any, Callable, Dict, Generic, List, Text,
                    Type, TypeVar, Union, cast, overload)

from sqlalchemy.ext.asyncio import async_scoped_session, create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession as _AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta, declared_attr
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm.decl_api import registry
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.dml import Delete, Insert, Update
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (BIGINT, DECIMAL, NUMERIC, BigInteger,
                                     Boolean, Date, DateTime, Float, Integer,
                                     String, Time)

from simple_starlette.ctx import g

logger = logging.getLogger("sqlalchemy_db")

D = TypeVar("D")
C = TypeVar("C")


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


mapper_register = registry()
_Base = mapper_register.generate_base(metaclass=BaseModelMeta)


class BaseModelDict(dict):
    __table_args__ = ()

    if TYPE_CHECKING:

        @classmethod
        def create_row(cls, **kwargs):
            return cls(**kwargs)


def row_obj_to_dict(
    obj,
    exclude_fields: List[str] = ["_sa_instance_state"],
    convert_func: List[Callable] = [],
):
    """orm 对象转为 dict

    exclude_fields: 排除不必要的字段
    convert_func: 进行一些数据操作，如 将 datetime 转换为 timestamp

    配合 partial 使用

    ```
    def somefunc(obj):
        d = obj.__dict__()
        ...
        return d
    to_dict = partial(to_dict, exclude_fields=['xxx'], convert_func=[somefunc])
    obj_dict = to_dict(obj)
    ```
    """

    obj_dict = obj.__dict__
    for k in exclude_fields:
        if k in obj_dict:
            obj_dict.pop(k)
    for _conver_f in convert_func:
        obj_dict = _conver_f(obj_dict)
    return obj_dict


class ColumnType(Generic[C], Column):
    if TYPE_CHECKING:

        def __add__(self, some) -> "ColumnType[C]":
            ...

        def __sub__(self, some) -> "ColumnType[C]":
            ...

        def __invert__(self) -> "ColumnType[C]":
            ...

        def __truediv__(self, some) -> "ColumnType[C]":
            ...

        def __floordiv__(self, some) -> "ColumnType[C]":
            ...

        def __mul__(self, some) -> "ColumnType[C]":
            ...

        def __rmul__(self, some) -> "ColumnType[C]":
            ...

        def __gt__(self, some) -> "ColumnType[C]":
            ...

        def __lt__(self, some) -> "ColumnType[C]":
            ...

        def __ge__(self, some) -> "ColumnType[C]":
            ...

        def __le__(self, some) -> "ColumnType[C]":
            ...

        def __eq__(self, some) -> "ColumnType[C]":
            ...

        def __ne__(self, some) -> "ColumnType[C]":
            ...


@overload
def column_field(
    column_type: Union[
        Type[Integer],
        Type[BIGINT],
        Type[BigInteger],
        BIGINT,
        BigInteger,
    ],
    primary_key: bool = False,
    default=None,
    nullable=None,
    comment=None,
    **kwargs,
) -> ColumnType[int]:
    ...


@overload
def column_field(
    column_type: Union[Type[Float], Type[DECIMAL], Type[NUMERIC]],
    primary_key: bool = False,
    default=None,
    nullable=None,
    comment=None,
    **kwargs,
) -> ColumnType[float]:
    ...


@overload
def column_field(
    column_type: Union[Type[Text], Type[String], String, Text],
    primary_key: bool = False,
    default=None,
    nullable=None,
    comment=None,
    **kwargs,
) -> ColumnType[str]:
    ...


@overload
def column_field(
    column_type: Union[Type[Boolean], Boolean],
    primary_key: bool,
    default=None,
    nullable=None,
    comment=None,
    **kwargs,
) -> ColumnType[bool]:
    ...


@overload
def column_field(
    column_type: Union[
        Type[DateTime], Type[Date], Type[Time], DateTime, Date, Time
    ],
    primary_key: bool = False,
    default=None,
    nullable=None,
    comment=None,
    **kwargs,
) -> ColumnType[datetime]:
    ...


def column_field(
    column_type,
    primary_key: bool = False,
    default=None,
    nullable=None,
    comment=None,
    **kwargs,
):
    return Column(
        column_type,
        primary_key=primary_key,
        default=default,
        nullable=nullable,
        comment=comment,
        **kwargs,
    )


BDC = TypeVar("BDC")


class Never:
    Ellipsis


R = TypeVar("R")

if TYPE_CHECKING:

    def register_db_model(cls: R) -> R:
        ...

else:

    def register_db_model(cls: R) -> R:
        def register_orm_model(orm_column_map):
            orm_column_map["create_row"] = classmethod(
                lambda _cls, **kwargs: _cls(**kwargs)
            )

            ModelClass = type(
                cast(
                    str,
                    getattr(
                        cls, "__tablename__", getattr(cls, "__name__")
                    ),
                ),
                (_Base,),
                orm_column_map,
            )
            return ModelClass

        fields_map = getattr(cls, "__dict__")
        orm_column_map = {}
        for _k, _v in fields_map.items():
            if _k in ["__module__", "__doc__"]:
                continue
            orm_column_map[_k] = _v

        if orm_column_map:
            return register_orm_model(orm_column_map)
        return cls


engines = {}


def split_read_write(clause, _flushing):
    # 读写分离
    # 默认 update onsert  insert 使用 master db
    # query 走 任一 db
    if bind_name := g.get("__ctx_bind_name"):
        return engines[bind_name].sync_engine

    if _flushing or isinstance(clause, (Update, Delete, Insert)):  # type: ignore
        return engines["master"].sync_engine
    else:
        return engines[
            random.choice(list(engines.keys()))
        ].sync_engine


class AsyncSession(_AsyncSession):
    if TYPE_CHECKING:

        def __call__(self, *args: Any, **kwds: Any) -> Session:
            return Session()

        def add(self, instance, _warn=True):
            ...

        def add_all(self, instance):
            ...

        def expire_all(self):
            ...

        def expire(self, instance, attribute_names=None):
            ...

        def expunge(self, instance):
            ...

        def expunge_all(self):
            ...


class Sqlalchemy:
    """
    init sqlalchemy
    """

    # ---config----
    MAIN_URI_NAME = "master"

    # 连接池大小（在连接池中保持打开的连接数），设置为 0，代表禁用连接池
    DB_POOL_SIZE: int = 30

    # 池在经过给定秒数后回收连接，默认为 -1 ，没有超时，，
    DB_POOL_RECYCLE: int = -1

    DB_POOL_MAX_OVERFLOW: int = 0

    # 设置数据库连接，最少必须设置  master
    DB_URIS: Dict[str, str] = {"master": "sqlite:///memory:"}
    # -----------

    # session instance
    _session = None

    # 读写分离插件
    split_read_write_ext = split_read_write

    # ping sql
    _ping_sql = "select 1"

    class RoutingSession(Session):
        def get_bind(self, mapper=None, clause=None, **kw):
            if Sqlalchemy.split_read_write_ext:
                return Sqlalchemy.split_read_write_ext(clause, self._flushing)  # type: ignore

    def __init__(self, app, **kwargs) -> None:
        """
        app -- simple-starlette app 实例
        async_io -- 使用异步io操作数据库
        """
        config_options = self.make_configs(app, kwargs)

        self.check_conf(config_options)

        self.create_engine_func = create_async_engine

        engines.update(self.create_engine(config_options))

        self.db_session_maker = sessionmaker(
            class_=AsyncSession,
            sync_session_class=self.RoutingSession,
            expire_on_commit=False,
            future=True,
        )

        self.session_factory_map = {}

    def check_conf(self, conf):
        uri_dict = conf["db_uris"]
        if self.MAIN_URI_NAME not in uri_dict:
            raise Exception(f"设置DB_URIS 时, {self.MAIN_URI_NAME}必须设置")

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
                uri_map[uri_name], **options, future=True
            )

        for _u in uri_map:
            _engine_create(_u)

        return engine_map

    @staticmethod
    def gen_scopefunc():
        def scopefunc():
            from asyncio import current_task

            try:
                return f"{current_task()}"
            except RuntimeError:
                return "__main_loop__"
            except Exception as e:
                raise e

        return scopefunc

    def set_ctx_db(self, name: str):
        """set default db on context
        db = Sqlalchemy(app)
        db.set_ctx_db("db_master")

        session = db.session()
        """
        if name not in engines:
            raise ValueError(
                f"db_name {name} not found, please check `db_uri` config"
            )
        g.__ctx_bind_name = name

    @property
    def session(self) -> AsyncSession:
        if self._session:
            return self._session()
        _session = async_scoped_session(
            self.db_session_maker, scopefunc=self.gen_scopefunc()
        )
        self._session = _session
        return self._session()

    @property
    def engines_iter(self):
        for _engine in engines.values():
            yield _engine

    async def create_all(self):
        async with engines["master"].begin() as conn:
            await conn.run_sync(_Base.metadata.create_all)
