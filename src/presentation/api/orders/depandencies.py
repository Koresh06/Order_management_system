from typing import Annotated
from dependency_injector.wiring import Provide, inject

from fastapi import Path, Depends, HTTPException, status

from src.application.containers.container import Container
from src.domain.entitys.order import OrderModel
from src.application.use_cases.base_use_case import BaseUseCase


@inject
def order_by_id(
    id: Annotated[int, Path],
    orders_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.orders_use_case]),
    ],
) -> OrderModel:
    order = orders_use_case.get_by_id(id)
    if order is not None:
        return order

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Order {id} not found!",
    )
