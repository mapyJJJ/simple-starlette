# Simple-Starlette

> 基于 Uvicorn 支持 HTTP/1.1 和 WebSockets

**一个简单的微服务api框架**: 在性能，可读性以及开发耗时上寻找一个最优解

---
- 支持定义`cbv`, `fbv`视图
- 请求参数添加类型注解，传参自动校验
- 自定义报错 , 全局报错/错误码 统一处理
- 提供请求内全局 `g` 对象 
- 更方便的定义 `websocket` api , 提供`websocket`鉴权方案
- 提供`include`划分不同接口，类似 `flask.blueprint`
- orm工具: `sqlalchemy.db`， 使用 `async.io` 特性，提供连接配置，开箱即用
- 缓存工具: `Memory Cache` , `Redis Cache` ,  适应不同业务场景
- `http_client`工具: 封装requests，如果业务需要接入第三方api时，有很大帮助
- `token-auth` , `cors` 中间件: 提供标准的 `jwt` 鉴权模式 cors配置
- `simple-api-doc`工具: 
    - 开发阶段提供类似swagger在线文档，方便前后端协作
    - 不同于swagger，它对业务代码结构完全无影响，只需要在开发阶段正常定义接口参数等，访问文档页面就会自定生成
- 原生支持sentry
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


