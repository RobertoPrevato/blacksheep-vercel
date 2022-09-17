import os
import platform
import sys

print("PYTHON VERSION: " + platform.python_version())
print("CURRENT FOLDER: " + os.getcwd())

blacksheep_files = [
    os.path.join(dp, f)
    for dp, _, filenames in os.walk(os.path.join(os.getcwd(), "blacksheep"))
    for f in filenames
]

for item in blacksheep_files:
    print(item)

sys.path.append(os.getcwd())

from blacksheep import Application, Content, Response

app = Application(show_error_details=True)
get = app.router.get


@get("/")
async def home() -> Response:
    return Response(200, content=Content(b"text/plain", b"Hello world :)"))
