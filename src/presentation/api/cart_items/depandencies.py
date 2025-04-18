from typing import Annotated
from dependency_injector.wiring import Provide, inject

from fastapi import Path, Depends, HTTPException

from src.domain.services.cart_item.cart_item_service_intarface import CartItemServiceInterface
# from src.application.containers.cart_item_container import CartItemContainer
from src.application.containers.main_container import MainContainer
from src.domain.entitys.cart_item import CartItemModel


@inject
def cart_by_id(
    id: Annotated[
        int,
        Path(
            title="User ID",
            description="Идентификатор пользователя",
            ge=1,
        )
    ],
    service: Annotated[
        CartItemServiceInterface,
        Depends(Provide[MainContainer.cart_item_service]),
    ],
) -> CartItemModel:
    """
    Зависимость для получения элемента корзины по идентификатору пользователя.

    Используется в эндпоинтах, где необходимо предварительно получить корзину.
    """
    try:
        return service.get_items_by_user(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Корзина не найдена: {e}")