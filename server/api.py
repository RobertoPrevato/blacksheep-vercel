from blacksheep import Application, Content, Response

app = Application(show_error_details=True)
get = app.router.get


@get("/")
async def home() -> Response:
    return Response(200, content=Content(b"text/plain", b"Hello world :)"))
