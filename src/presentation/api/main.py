from fastapi import FastAPI

from src.application.containers.order_container import OrderContainer
from src.application.containers.user_container import UserContainer
from src.application.containers.category_container import CategoryContainer
from src.application.containers.item_container import ItemContainer
from src.application.containers.cart_item_container import CartItemContainer
from src.application.containers.main_container import MainContainer

from src.presentation.api.users.router import router as users_router
from src.presentation.api.items.router import router as item_router
from src.presentation.api.categories.router import router as category_router
from src.presentation.api.cart_items.router import router as cart_router
from src.presentation.api.orders.router import router as order_router



def create_app() -> FastAPI:
    # user_container = UserContainer()
    # user_container.wire(modules=["src.presentation.api.users.router"])

    # category_container = CategoryContainer()
    # category_container.wire(modules=["src.presentation.api.categories.router"])

    # item_container = ItemContainer()
    # item_container.wire(modules=["src.presentation.api.items.router"])

    # cart_item_container = CartItemContainer()
    # cart_item_container.wire(modules=["src.presentation.api.cart_items.router"])

    # order_container = OrderContainer(cart_item_service=cart_item_container.cart_item_service)
    # order_container.wire(modules=["src.presentation.api.orders.router"])

    main_container = MainContainer()
    main_container.wire(modules=[
        "src.presentation.api.users.router",
        "src.presentation.api.items.router",
        "src.presentation.api.categories.router",
        "src.presentation.api.cart_items.router",
        "src.presentation.api.orders.router",
    ])

    app = FastAPI(
        title="API",
        description="API",
        version="1.0.0",
    )
    
    app.include_router(users_router)
    app.include_router(item_router)
    app.include_router(category_router)
    app.include_router(cart_router)
    app.include_router(order_router)

    return app
