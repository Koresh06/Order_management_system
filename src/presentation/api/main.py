from fastapi import FastAPI

from src.application.containers.container import Container
from src.presentation.api.users.router import router as users_router


def create_app() -> FastAPI:
    container = Container()
    container.wire(modules=["src.presentation.api.users.router"])
    app = FastAPI(
        title="API",
        description="API",
        version="1.0.0",
    )
    app.include_router(users_router)

    return app
