from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

# from src.application.containers.order_container import OrderContainer
from src.application.containers.main_container import MainContainer
from src.domain.entitys.user import UserModel
from src.domain.services.order.order_service_intarface import OrderServiceInterface
from src.domain.use_case.intarface import UseCaseOneEntity
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.presentation.api.orders.depandencies import order_by_id
from src.presentation.api.orders.schemas import OrderCreateSchema, OrderOutSchema
from src.presentation.api.users.depandencies import user_by_id


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


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=list[OrderOutSchema],
    summary="Получить заказы пользователя",
    description="Возвращает список всех заказов пользователя.",
)
@inject
def get_all_orders_by_user(
    user: Annotated[
        UserModel,
        Depends(user_by_id),
    ],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[MainContainer.get_all_orders_by_user_use_case]),
    ],
) -> list[OrderOutSchema]:
    try:
        return use_case.execute(user.id)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_all_orders_by_user", e)
    

@router.get(
    "/{order_id}",
    status_code=status.HTTP_200_OK,
    response_model=OrderOutSchema,
    summary="Получить заказ",
    description="Возвращает заказ по его ID.",
)
@inject
def get_order_by_id(
    order: Annotated[
        OrderServiceInterface,
        Depends(order_by_id),
    ],
) -> OrderOutSchema:
    try:
        return order
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_order_by_id", e)


@router.get(
    "/",
    response_model=list[OrderOutSchema],
    summary="Получить все заказы",
    description="Для админов: возвращает список всех заказов в системе.",
)
@inject
def get_all_orders(
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[MainContainer.get_all_orders_use_case]),
    ],
) -> list[OrderOutSchema]:
    try:
        return use_case.execute()
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_all_orders", e)



@router.delete(
    "/{order_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить заказ",
    description="Удаляет заказ из базы данных по его ID.",
)
@inject
def delete_order(
    order: Annotated[
        OrderServiceInterface,
        Depends(order_by_id),
    ],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[MainContainer.canclel_order_use_case]),
    ],
) -> None:
    try:
        use_case.execute(order)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in delete_order", e)
