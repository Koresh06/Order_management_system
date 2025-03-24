from fastapi import FastAPI

from src.application.containers.container import Container
from src.presentation.api.users.router import router as users_router
from src.presentation.api.roles.router import router as roles_router
from src.presentation.api.item.router import router as item_router



def create_app() -> FastAPI:
    container = Container()
    container.wire(
        modules=[
            "src.presentation.api.users.router",
            "src.presentation.api.roles.router",
            "src.presentation.api.item.router",
        ]
    )
    app = FastAPI(
        title="API",
        description="API",
        version="1.0.0",
    )
    app.include_router(users_router)
    app.include_router(roles_router)
    app.include_router(item_router)

    return app
