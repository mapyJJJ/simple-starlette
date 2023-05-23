# Simple-Starlette

[![License](https://img.shields.io/static/v1?label=asgi&message=starlette&color=red)]()
[![License](https://img.shields.io/static/v1?label=asgi-server&message=uvicorn&color=green)]()
[![License](https://img.shields.io/static/v1?label=imports&message=isort&color=origin)]()
[![License](https://img.shields.io/static/v1?label=format&message=black&color=origin)]()
[![License](https://img.shields.io/static/v1?label=type-hint&message=pyright&color=origin)]()

**python微服务框架**: 
- 高性能 : asyncio + Uvicorn 高性能异步非阻塞io，事件循环，多路监听 
- 可读性 : 请求与视图解耦，视图与Service解耦，文档与业务解耦
- 开发耗时: 多种基础工具和中间件，类似flask的开发体验

---

### 安装使用

1, 使用 `pip` 直接安装

```bash
pip install simple-starlette
```

2, 源码安装
```bash
git clone https://github.com/mapyJJJ/simple-starlette.git
cd simple-starlette
python3 setup.py install
```

---

### hello world:

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
查看更多开发使用实例：[example usage](https://github.com/mapyJJJ/simple-starlette/tree/master/example)

---
#### LICENSE

[GPL-3.0 License](https://github.com/mapyJJJ/simple-starlette/blob/master/LICENSE)

---
