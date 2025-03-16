from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from src.application.containers.container import Container
from src.presentation.api.orders.schemas import OrderOutSchema
from src.application.use_cases.base_use_case import BaseUseCase


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


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