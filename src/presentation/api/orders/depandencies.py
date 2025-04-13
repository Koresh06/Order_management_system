from fastapi import Path, Depends, HTTPException, status
from typing import Annotated
from dependency_injector.wiring import Provide, inject

from src.application.containers.main_container import MainContainer
from src.domain.services.order.order_service_intarface import OrderServiceInterface
from src.domain.entitys.order import OrderModel


@inject
def order_by_id(
    order_id: Annotated[
        int,
        Path(
            title="Order ID",
            description="Идентификатор заказа",
            ge=1,
        )
    ],
    service: Annotated[
        OrderServiceInterface,
        Depends(Provide[MainContainer.order_service]),
    ],
) -> OrderModel:
    """
    Получить заказ по ID. Используется как зависимость.

    - **order_id**: ID пользователя
    """
    order = service.get_by_id(order_id)
    if order is not None:
        return order

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с ID {order_id} не найден.",
    )
