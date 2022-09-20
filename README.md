# Simple-Starlette
---
> 基于 Uvicorn 支持 HTTP/1.1 和 WebSockets

**一个简单的微服务 api 框架**: 
- 高性能 : asyncio + Uvicorn 高性能异步非阻塞io，事件循环，多路监听 
- 可读性 : 请求与视图解耦，视图与Service解耦，文档与业务解耦
- 开发耗时: 多种基础工具和中间件，类似flask的开发体验
---

- **基础功能**:
  - [x] 支持不同编码习惯来定义视图函数(类视图，函数视图), 直接写类方法函数方法搭配语法糖
  - [x] 支持用户封装请求参数为固定对象，每个参数根据注解自动进行校验等操作，随后发送至对应视图函数，用户只需要定义一个参数接收此对象，仅需要将该参数注解类型指定为该对象即可
  - [x] 支持 Include 对象，用于对接口进行分组
  - [x] 支持 aio sqlalchemy ，主从配置，读写分离, 会话管理
  - [x] 支持 在线 api 文档，自研文档项目 `simple-api-doc`, 为开发者自动生成在线文档
    - [x] `simple-api-doc`: 完成分组展示，单个接口详情展示，用户注释 , 请求参数展示, 正常响应参数展示
    - [ ] `simple-api-doc`: 在线模拟 http 请求(cookie，参数设定，真实响应展示)
    - [ ] `simple-api-doc`: 主动捕获接口中用户定义的错误码，自动生成展示
    - [ ] ...

  - [x] 中间件支持，asgi 协议下，一个对象只要能够接收(Scope, Send, Receive)这三个参数，并且在处理完自身逻辑后继续调用下一个中间件，继续传递这三个参数，直到最后被视图函数接收，例如ExceptionMiddleware，处于最外层，用于捕获全局抛出的任何错误
    - [x] cors 跨域设置中间件
    - [x] token_auth 标准 jwt 鉴权中间件
    - [ ] api rate limiter
    - [x] 还有很多中间件用于搭配第三方工具日志收集，指标收集，链路追踪等等，都可以去它们各自的 sdk 中找到现成的基于 asgi 的中间件代码
    - [ ] ....
  - [x] 支持 ws 长连接接口的定义
    - [ ] wss 加密支持
  - [x] jsonrpc
  - [x] 上下文变量与视图解耦，flask的Context对象对于防止循环引用以及参数长传有很好的改善效果
    - [x] `g` ,  `request` , `current_app` , `app.context_app`
---


- **其他功能**:
  - [x] 二级缓存 : `guava cache` , `lru ttl cache`
  - [x] httpclient: http客户端用于对接第三方平台OpenApi，
    - [x] before_request , after_request, retry
    - [ ] aio client ,上面的实现本质上是 io阻塞的
---

#### 安装

使用 `pip` 直接安装

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

---