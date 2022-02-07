from .main import dispatch as dispatch
from http.server import BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None: ...

def serve(name: str=..., port: int=...) -> None: ...
