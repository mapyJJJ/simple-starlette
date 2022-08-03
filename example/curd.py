# fbv （函数视图）使用方法
from typing import Optional

from requests.sessions import Request
from starlette.requests import Request

from simple_starlette import Response, ResTypeEnum, SimpleStarlette
from simple_starlette.args import BodyParams, QueryParams, register_args

app = SimpleStarlette(__name__)

@register_args
class IndexQuery(QueryParams):
    # 如果定义query参数，请直接继承QueryParams
    a: str
    b: int

@register_args
class IndexBody(BodyParams):
    # 如果定义body参数，请直接继承QueryParams
    x: str
    y: int

@register_args
class IndexBody2(BodyParams):
    # 如果参数在业务层有区分，也可以定义多个 Params 类
    x2: Optional[str]
    y2: Optional[int]

@app.route("/index/{user_id:int}", allow_methods=["GET", "POST"])
def index(request: Request, q: IndexQuery, b: IndexBody, b2: IndexBody2): # 请将所有需要客户端发送过来的参数，作为入参定义在此处，内部直接操作这些参数即可
    # request 必须作为第一个参数被传入，里面包含当前请求的相关信息，具体属性方法直接跳到 `Request`  查看
    print(request.path_params["user_id"])
    if request.method == "GET":
        print(q.a, q.b)  # 直接作为对象操作，获取参数
    else:
        print(b.x, b.y, b2.x2, b2.y2)

    return Response({"url": str(request.url)}, ResTypeEnum.JSON) # 构造所需的返回类型，支持 text，html, json, file等


if __name__ == "__main__":
    app.run(port=5000)