# sqlalchemy-db

import asyncio
from typing import NamedTuple, cast, List


from simple_starlette import (
    Response,
    ResTypeEnum,
    SimpleStarlette,
    Request,
    QueryParams,
)
from simple_starlette.db.db_sqlalchemy import (
    BaseModelDict,
    Sqlalchemy,
    column_field,
    register_db_model,
    String,
    Integer,
    select,
    count,
    Label,
    Index,
)

# 初始化app
app = SimpleStarlette(__name__)

# NOTICE!! 提供mysql的配置, 驱动为asyncmy, 不要更改, 一般需要写入到 config 文件中，而不是硬编码
app.config["DB_URIS"] = {
    "master": "mysql+asyncmy://root:123123@1.1.1.1:3306/test"
}

# NOTICE!! 初始化db
db = Sqlalchemy(app)


# NOTICE!! 请求结束后执行session.close(),将连接放回到连接池中
@app.after_request
async def _do_after_request(request, response):
    await db.session.close()
    return response


# 创建表映射
# 映射三张表 Person, Person1, Person2
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


# 创建http接口
@app.route("/test_db/add", ["GET"])
class TestDbAdd:
    class PersonParams(QueryParams):
        email: str

    async def get(self, _: Request, person_args: PersonParams):
        """
        测试插入数据
        """
        new_person = Person.create_row(email=person_args.email)
        new_person1 = Person1.create_row(email=person_args.email)
        db.session.add(new_person)
        db.session.add(new_person1)

        await db.session.commit()

        return Response(
            {"id": new_person.id, "email": new_person.email},
            ResTypeEnum.JSON,
        )


@app.route("/test_db/one", ["GET"])
async def test_db(request: Request):
    """
    测试查询
    场景： 查询一行数据以及表中数据的总行数
    """

    async def query_one_person():
        # sync result
        result = await db.session.execute(
            select(Person.id).order_by(Person.id.desc())
        )
        first_p_id = result.scalars().first()
        # async result
        # result = await db.session.stream(
        #     select(Person).order_by(Person.id.desc())
        # )
        # first_p_id = await result.scalars().first()
        return first_p_id

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

    person_instance_id, total_count = await query()
    return Response(
        {"max_id": person_instance_id, "total_count": total_count},
        ResTypeEnum.JSON,
    )


@app.route("/test_db/join_query", allow_methods=["get"])
async def test_db_join_query(request: Request):
    """
    join
    """
    result = await db.session.execute(
        select(Person.email, Person1.id).join(  
            Person1.id, Person.id == Person1.id
        )
    )
    class _R(NamedTuple):
        email: str
        id: int
    res = cast(List[_R], result.all())[0]
    return Response({"email": res.email, "id": res.id}, ResTypeEnum.JSON)


@app.route("/test_db/create_all", allow_methods=["get"])
async def test_db_create_all(request: Request):
    """
    可以通过create_all , 帮助创建表
    """
    await db.create_all()
    return Response("ok", ResTypeEnum.TEXT)


if __name__ == "__main__":
    app.run(host="0.0.0.0")