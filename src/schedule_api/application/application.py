from fastapi import FastAPI
from fastapi.responses import ORJSONResponse


def create_app() -> FastAPI:
    app = FastAPI(default_response_class=ORJSONResponse)

    return app


app = create_app()
