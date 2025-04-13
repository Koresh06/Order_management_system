from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

# from src.application.containers.order_container import OrderContainer
from src.application.containers.main_container import MainContainer    
from src.domain.use_case.intarface import UseCaseOneEntity
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.presentation.api.orders.schemas import OrderCreateSchema, OrderOutSchema


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OrderOutSchema,
    summary="Создать заказ",
    description="Создает новый заказ и добавляет его в базу данных.",
)
@inject
def create_order(
    order: OrderCreateSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[MainContainer.create_order_use_case]),
    ],
) -> OrderOutSchema:
    try:
        return use_case.execute(order)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in create_order", e)


