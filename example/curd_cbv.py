# 定义cbv类型视图

from simple_starlette.args import QueryParams
from simple_starlette import SimpleStarlette, Request
from simple_starlette.responses import Response, ResTypeEnum

app = SimpleStarlette(__name__)

@app.route("/index")
class Index:
    class IndexQuery(QueryParams):
        a: int
        b: int

    # 定义 get 方法
    async def get(self, request: Request, q: IndexQuery):
        return Response({"a": q.a, "b": q.b}, ResTypeEnum.JSON)
    
if __name__ == "__main__":
    app.run()