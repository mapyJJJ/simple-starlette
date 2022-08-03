# --json-rpc-client--
import asyncio

from simple_starlette.rpc.json_rpc import JsonRpcClient


async def main():
    PingServer = JsonRpcClient(
        host="http://127.0.0.1:5001/",
        method="post",
        method_name="ping",
    )
    r = await PingServer.get_response(params={"name": "jack"})
    print(r.result)  # pong jack


asyncio.run(main())
