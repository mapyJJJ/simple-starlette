import asyncio
from typing import NamedTuple, cast, List

from sqlalchemy import func


from simple_starlette import (
    Response,
    ResTypeEnum,
    SimpleStarlette,
    Request,
    QueryParams,
    logger,
)
from simple_starlette.db.db_sqlalchemy import (
    BaseModelDict,
    Sqlalchemy,
    column_field,
    register_db_model,
    String,
    Integer,
    row_obj_to_dict,
    select,
    Index,
)

# 初始化app
app = SimpleStarlette(__name__)

# NOTICE!! 提供mysql的配置, 驱动为asyncmy, 不要更改, 一般需要写入到 config 文件中，而不是硬编码
app.config["DB_URIS"] = {
    "master": "mysql+asyncmy://root:@127.0.0.1:3306/test"
}
logger = logger.getLogger(__name__)

db = Sqlalchemy(app)

# 映射三张表 Person, Person1, Person2
@register_db_model
class Person(BaseModelDict):
    id = column_field(Integer, primary_key=True)
    email = column_field(String(64))
    __table_args__ = (Index("idx_email", "email"),)

@app.route("/test_db/add", ["GET"])
class TestDbAdd:
    class PersonParams(QueryParams):
        email: str

    async def get(self, _: Request, person_args: PersonParams):
        """
        插入数据
        """
        async with db.session as session:
            new_person = Person.create_row(email=person_args.email)
            session.add(new_person)
            await session.commit()
            
        return Response(
            {"id": new_person.id, "email": new_person.email},
            ResTypeEnum.JSON,
        )

@app.route("/test_db/list", ["GET"])
async def test_db(request: Request):
    """
    测试查询
    场景： 查询一行数据以及表中数据的总行数
    """

    async def query_list():
        async with db.session as session:
            result = await session.execute(select(Person).order_by(Person.id.desc()))
            ps = result.scalars()
        logger.info(ps)
        return ps

    async def query_count():
        async with db.session as session:
            result = await session.execute(select(func.count(Person.id)))
            count = result.scalar()
        return count

    async def query():
        L = await asyncio.gather(
            query_list(), query_count()
        )
        return L

    ps, total_count = await query()
    return Response(
        {"person_list": [row_obj_to_dict(p) for p in ps], "total_count": total_count},
        ResTypeEnum.JSON,
    )

@app.route("/test_db/create_all", allow_methods=["get"])
async def test_db_create_all(request: Request):
    """
    可以通过create_all , 帮助创建表
    """
    await db.create_all()
    return Response("ok", ResTypeEnum.TEXT)


if __name__ == "__main__":
    app.run(host="0.0.0.0")