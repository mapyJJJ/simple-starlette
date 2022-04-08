from starlette.websockets import WebSocket
from simple_starlette import SimpleStarlette

app = SimpleStarlette(__name__)


@app.route("/ws", websocket_route=True)
async def test(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        if data == "ok":
            break
        await websocket.send_text(f"xxx: {data}")

app.run()