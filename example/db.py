import asyncio
from simple_starlette.args import QueryParams

from sqlalchemy import Column, Integer, String, select
from sqlalchemy.sql.elements import Label
from sqlalchemy.sql.functions import count
from starlette.requests import Request


from simple_starlette.db.db_sqlalchemy import DbBaseModel, Sqlalchemy
from simple_starlette import (
    Response,
    ResTypeEnum,
    SimpleStarlette,
    register_args,
)

app = SimpleStarlette(__name__)
app.config["DB_URIS"] = {
    "master": "mysql+aiomysql://root:123456@localhost/testss?charset=utf8mb4"  # 改为自己的 连接地址进行测试
}

# app.load_conf_from_file("example/self_config.py")
db = Sqlalchemy(app)


class Person(DbBaseModel["Person"]):
    id = Column(Integer, primary_key=True)
    email = Column(String(64))


@register_args
class PersonParams(QueryParams):
    email: str


# test query table
@app.route("/test_db", allow_methods=["get"])
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


# test add data
@app.route("/test_db/add", allow_methods=["get"])
async def test_db_add(request: Request, person_args: PersonParams):
    async def add_one_person():
        new_person = Person.create(email=person_args.email)
        db.session.add(new_person)
        await db.session.commit()
        return new_person

    p = await add_one_person()
    return Response({"id": p.id, "email": p.email}, ResTypeEnum.JSON)


if __name__ == "__main__":
    app.run(port=5001)
