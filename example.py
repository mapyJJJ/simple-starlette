from simple_starlette import SimpleStarlette

app = SimpleStarlette(__name__)

@app.route("/get_one")
class GetOne:
    def get(self, request):
        pass