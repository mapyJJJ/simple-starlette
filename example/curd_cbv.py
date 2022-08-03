# cbv

from simple_starlette import SimpleStarlette, Request
from simple_starlette.args import QueryParams
from simple_starlette.responses import Response, ResTypeEnum

app = SimpleStarlette(__name__)

# 推荐使用这种方式 
@app.route("/index")
class Index:
    class IndexQuery(QueryParams):
        a: int
        b: int

    async def get(self, request: Request, q: IndexQuery): # 定义 get 方法
        return Response({"a": q.a, "b": q.b}, ResTypeEnum.JSON)
    

app.run()