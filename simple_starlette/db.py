# db.py
# base on: sqlalchemy
# ~~~~~~~~~~~~~

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Person(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(64))


engine = create_async_engine(
    "mysql+aiomysql://root:wszsd@localhost/testss?charset=utf8mb4"
)

conntion = engine.connect()

conntion.sync_connection