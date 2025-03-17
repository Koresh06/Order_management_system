from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from src.application.containers.container import Container
from src.presentation.api.orders.schemas import OrderOutSchema, OrderCreateSchema, OrderUpdateSchema, OrderUpdatePartilSchema
from src.application.use_cases.base_use_case import BaseUseCase
from src.presentation.api.orders.depandencies import order_by_id


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderOutSchema,
)
@inject
def create_order(
    order_create: OrderCreateSchema,
    orders_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.orders_use_case]),
    ],
):
    order = orders_use_case.create(order_create)
    return OrderOutSchema.model_validate(order)



@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[OrderOutSchema],
)
@inject
def get_orders(
    users_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.users_use_case]),
    ],
) -> list[OrderOutSchema]:
    users = users_use_case.get_all()
    return [OrderOutSchema.model_validate(user) for user in users]


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=OrderOutSchema,
)
@inject
def get_order_by_id(
    order: Annotated[
        OrderOutSchema,
        Depends(order_by_id),
    ],
) -> OrderOutSchema:
    return OrderOutSchema.model_validate(order)


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=OrderOutSchema,
)
@inject
def replace_order(
    order_update: OrderUpdateSchema,
    order: Annotated[
        OrderOutSchema,
        Depends(order_by_id),
    ],
    orders_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.orders_use_case]),
    ],
):
    order = orders_use_case.update(
        order=order,
        order_update=order_update,
    )
    return OrderOutSchema.model_validate(order)


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=OrderOutSchema,
)
@inject
def modify_order(
    order_update: OrderUpdatePartilSchema,
    order: Annotated[
        OrderOutSchema,
        Depends(order_by_id),
    ],
    orders_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.orders_use_case]),
    ],
):
    order = orders_use_case.update(
        order=order,
        order_update=order_update,
        partial=True,
    )
    return OrderOutSchema.model_validate(order)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
def delete_order(
    order: Annotated[
        OrderOutSchema,
        Depends(order_by_id),
    ],
    orders_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.orders_use_case]),
    ],
):
    orders_use_case.delete(order.id)