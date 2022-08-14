#--WebSocket-Example--
"""
在SimpleStarlette中使用基于tcp双工通信的websocket接口
"""

from starlette.websockets import WebSocket

from simple_starlette import SimpleStarlette

app = SimpleStarlette(__name__)

@app.route("/ws", websocket_route=True)
async def test(websocket: WebSocket):
    # websocket没有官方默认的鉴权方案
    # 用户完全可以自己很方便的实现
    # 在 accept 前也就是http 101 握手协议转为 tcp的过程 
    # 完全可以在这里通过http headers 或者 cookies进行建立连接阶段的鉴权逻辑
    # 至于数据传输阶段，可以适当的使用 token机制防止重放攻击
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data == "close_conn":
            break
        await websocket.send_text(f"xxx: {data}")

if __name__ == "__main__":
    app.run()