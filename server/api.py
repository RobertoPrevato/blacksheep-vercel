from blacksheep import Application, Content, Response

app = Application()
get = app.router.get


@get("/")
async def home() -> Response:
    return Response(
        200,
        content=Content(
            b"text/plain",
            b"Hello world :)"))
