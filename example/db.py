import asyncio
from typing import TYPE_CHECKING

from sqlalchemy.sql.schema import Index
from simple_starlette.args import QueryParams

from sqlalchemy import Integer, String, select
from sqlalchemy.sql.elements import Label
from sqlalchemy.sql.functions import count
from starlette.requests import Request

from simple_starlette.db.db_sqlalchemy import (
    BaseModelDict,
    Sqlalchemy,
    column_field,
    register_db_model
)
from simple_starlette import (
    Response,
    ResTypeEnum,
    SimpleStarlette,
    register_args,
)

app = SimpleStarlette(__name__)

app.load_conf_from_file("example/self_config.py")
db = Sqlalchemy(app)


@register_db_model
class Person(BaseModelDict):
    id = column_field(Integer, primary_key=True)
    email = column_field(String(64))

    __table_args__ = (Index("idx_email", "email"),)


@register_db_model
class Person1(BaseModelDict):
    id = column_field(Integer, primary_key=True)
    email = column_field(String(64))

    __table_args__ = (Index("idx_email", "email"),)


@register_db_model
class Person2(BaseModelDict):
    id = column_field(Integer, primary_key=True)
    email = column_field(String(64))

    __table_args__ = (Index("idx_email", "email"),)


@register_args
class PersonParams(QueryParams):
    email: str


@app.route("/test_db/one", allow_methods=["get"])
async def test_db(request: Request):
    async def query_one_person():
        r = await db.session.execute(
            select(Person).order_by(Person.id.desc())
        )
        fisrt_p = r.scalars().first()
        return fisrt_p

    async def query_person_count():
        r = await db.session.execute(
            select(Label("count", count(Person.id)))
        )
        return r.scalar()

    async def query():
        L = await asyncio.gather(
            query_one_person(), query_person_count()
        )
        return L

    person_instance, total_count = await query()
    return Response(
        {"max_id": person_instance.id, "total_count": total_count},
        ResTypeEnum.JSON,
    )

@app.route("/test_db/add", allow_methods=["get"])
async def test_db_add(request: Request, person_args: PersonParams):
    new_person = Person.create_row(email=person_args.email)
    db.session.add(new_person)
    await db.session.commit()
    return Response(
        {"id": new_person.id, "email": new_person.email},
        ResTypeEnum.JSON,
    )


@app.route("/test_db/create_all", allow_methods=["get"])
async def test_db_create_all(request: Request):
    await db.create_all()
    return Response("ok", ResTypeEnum.TEXT)


if __name__ == "__main__":
    app.run(port=5001)
