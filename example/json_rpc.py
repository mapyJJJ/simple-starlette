from simple_starlette import SimpleStarlette
from simple_starlette.rpc.json_rpc import JsonRpcServer

app = SimpleStarlette(__name__)

rpc_server = JsonRpcServer(app)


@rpc_server.register_rpc_method(name="ping")
def ping(name):
    return rpc_server.to_response(f"pong {name}")


if __name__ == "__main__":
    rpc_server.run(port=5001)

    
####client


import asyncio
from simple_starlette.rpc.json_rpc import JsonRpcClient

async def main():
    PingServer = JsonRpcClient(host='http://127.0.0.1:5001/', method="post", method_name='ping')
    r = await PingServer.get_response(params={"name": "jack"})
    print(r.result)  # pong jack

asyncio.run(main())