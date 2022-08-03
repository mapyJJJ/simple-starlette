# --json-rpc--
# 本质还是基于http

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
