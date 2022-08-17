# Simple-Starlette

> 基于 Uvicorn 支持 HTTP/1.1 和 WebSockets

**一个简单的微服务api框架**: 在性能，可读性以及开发耗时上寻找一个最优解

---

- 基础功能:
    - `cbv, fbv` , 不同写法定义视图函数
    - `api依赖参数导入`, 使用python3类型注解的方式将参数注入到自定义的参数中
    - `exception全局错误自定义`
    - `G`, request context g 
    - `websocket` 
    - `include` 对象，为api划分层级
    - `simple-api-doc` 自动生成 , 在线api文档

- 其他功能:
    - `orm.sqlalchemy. async.io` 支持
    - `local_cache` : `guava cache` ,`lru cache`
    - `http_client` 对接第三方api
    - `MiddleWare.TokenAuth` jwt 中间件
    - `starlette`上所有中间件都可以使用(如 sentry, prometheus, ...)
    
---

#### 安装

使用 `pip`  直接安装
```bash
pip install simple-starlette
```

---

#### A Simple Example:

```python
from simple_starlette.args import QueryParams
from simple_starlette import SimpleStarlette, Request
from simple_starlette.responses import Response, ResTypeEnum

app = SimpleStarlette(__name__)

@app.route("/test")
class Index:
    class SomeQuery(QueryParams):
        arg1: int
        arg2: int

    async def get(self, request: Request, q: SomeQuery):  # 定义一个get请求
        return Response({"arg1": q.arg1, "arg2": q.arg2}, ResTypeEnum.JSON) # 构造返回json字符串
    
if __name__ == "__main__":
    app.run()

# 测试请求
# curl http://localhost:9091/test?arg1=hello&arg2=world
# response: 
# {"arg1":"hello", "arg2":"world"}
```

查看更多实例: [example usage](https://github.com/mapyJJJ/simple-starlette/tree/master/example)



---
#### LICENSE
[GPL-3.0 License](https://github.com/mapyJJJ/simple-starlette/blob/master/LICENSE)


