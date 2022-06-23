# Simple-Starlette

---

**一个简单的微服务api框架，基于 `starlette` 框架实现**：


- 支持视图模式：`cbv`, `fbv` 
- 请求参数添加类型注解，参数自动校验
- 全局错误处理
- 开箱即用 `websocket`
- 提供请求内全局临时  `g` 对象 
- `include` 类 `flask.blueprint`
- 数据库 `sqlalchemy.db`， 使用 `async.io` 特性，提供连接配置，开箱即用
- 缓存提供  `Memory Cache` , `Redis Cache` ,  适应不同业务场景，部署方式
- 提供http_client 模块 ，基于 requests 提供`before`, `after` 钩子
- `token-auth` 中间件，提供标准的 `jwt` 鉴权模式
---

#### 安装

使用 `pip`  直接安装
```bash
pip install simple-starlette
```

---

#### example

[example usage](example.md)

---
#### LICENSE
[GPL-3.0 License](https://github.com/mapyJJJ/simple-starlette/blob/master/LICENSE)


