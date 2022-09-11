# API

To build, use:

```sh
gunicorn -k uvicorn.workers.UvicornWorker server.api:app
```
