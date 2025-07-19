from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from sсhedule_api.infrastructure.di.ioc import create_container


def create_app() -> FastAPI:
    container = create_container()

    app_ = FastAPI(default_response_class=ORJSONResponse)

    setup_dishka(
        container=container,
        app=app_,
    )

    return app_


app = create_app()
