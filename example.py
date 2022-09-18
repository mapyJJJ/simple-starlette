from typing import List, Optional

from pydantic import BaseModel, Field, root_validator

from simple_starlette import Include, Request, SimpleStarlette
from simple_starlette.args import (BodyParams, QueryParams, ResponseParams,
                                   register_args)
from simple_starlette.middleware.cors import CorsMiddlewareGenFunc
from simple_starlette.responses import Response, ResTypeEnum
from simple_starlette.exceptions import RequestArgsNoMatch

app = SimpleStarlette(
    __name__,
    run_env="dev",  # dev模式开启在线文档
    middleware=[CorsMiddlewareGenFunc(allow_origins=["*"])],
)

# include api
api_user = Include(app, "/api/user")
api_admin = Include(app, "/api/admin")


@register_args()
class GetAdminOrUserOneArgs(QueryParams):
    """
    通过 id 或 name 查询admin
    """

    id_: Optional[int] = Field(description="id_ 和 name 必传其中一个")
    name: Optional[str]

    @root_validator
    def validate_all(cls, values):
        if not (values["name"] or values["id_"]):
            raise RequestArgsNoMatch("id_ 和 name不能全为空")
        return values


@api_admin.route("/one", allow_methods=["GET"])
async def get_admin_one(
    requset: Request, query_args: GetAdminOrUserOneArgs
):
    """
    获取admin详情接口
    """
    # --do-something--
    return Response(
        {"admin_id": query_args.id_, "admin_name": query_args.name},
        ResTypeEnum.JSON,
    )


class GetAdminListArgs(QueryParams):
    offset: int = 0
    limit: int = 20


class AdminOneArgs(BaseModel):
    admin_id: int
    admin_name: str


class GetAdminListResponse(ResponseParams):
    success_code: int = 200
    message: str
    admin_list: List[AdminOneArgs]


@api_admin.route("/list", allow_methods=["GET"])
async def get_admin_list(
    request: Request,
    query_args: GetAdminListArgs,
    _: GetAdminListResponse,
):
    """
    获取admin列表数据
    """
    # --do-something--
    return Response(
        {
            "success_code": 200,
            "message": "success",
            "admin_list": [{"admin_id": 1, "admin_name": "name"}],
        },
        ResTypeEnum.JSON,
    )


@api_user.route("/one")
class GetUserOne:
    class ResponseArgs(ResponseParams):
        """
        user one 返回值
        """

        class ResponseUserItem(BaseModel):
            name: str
            age: int
            id_: int

        message: str = Field(description="状态值")
        status_code: int = Field(description="状态码")
        user: ResponseUserItem = Field(description="user对象")

    class PostArgs(BodyParams):
        name: str = "jack"

    def get(
        self,
        request: Request,
        query: GetAdminOrUserOneArgs,
        _: ResponseArgs,
    ):
        """
        获取user详情接口
        """
        # --do-something--
        return Response(
            {
                "status_code": 200,
                "message": "success",
                "user": {"name": "user", "id_": 1, "age": 19},
            },
            ResTypeEnum.JSON,
        )


if __name__ == "__main__":
    app.run()
