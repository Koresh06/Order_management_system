from fastapi import FastAPI

from src.application.containers.user_container import UserContainer
from src.presentation.api.users.router import router as users_router
from src.presentation.api.items.router import router as item_router
from src.presentation.api.categories.router import router as category_router
from src.presentation.api.carts.router import router as cart_router



def create_app() -> FastAPI:
    user_container = UserContainer()
    user_container.wire(modules=["src.presentation.api.users.router"])

    app = FastAPI(
        title="API",
        description="API",
        version="1.0.0",
    )
    
    app.include_router(users_router)
    app.include_router(item_router)
    app.include_router(category_router)
    app.include_router(cart_router)

    return app
