from typing import Annotated
from fastapi import APIRouter, Depends, Query, status
from pydantic import Field
from dependency_injector.wiring import Provide, inject

from src.domain.services.cart_item.cart_item_service_intarface import CartItemServiceInterface
from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.application.containers.cart_item_container import CartItemContainer
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.presentation.api.cart_item.depandencies import cart_by_id
from src.presentation.api.cart_item.schemas import (
    CartItemOutSchema,
    CartItemCreateSchema,
    CartItemUpdateSchema,
    CartItemUpdatePartialSchema,
)


router = APIRouter(
    prefix="/cart-items",
    tags=["Cart Items"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CartItemOutSchema,
    summary="Добавить товар в корзину",
    description="Создает новый элемент корзины для указанного пользователя и товара.",
)
@inject
def add_cart_item(
    cart_item: CartItemCreateSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[CartItemContainer.add_cart_item_use_case]),
    ],
) -> CartItemOutSchema:
    """
    Добавить товар в корзину пользователя.

    - **user_id**: ID пользователя
    - **item_id**: ID товара
    - **quantity**: Количество
    """
    try:
        return use_case.execute(cart_item)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in add_cart_item", e)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CartItemOutSchema],
    summary="Получить все товары в корзине пользователя",
    description="Возвращает список всех элементов корзины для указанного пользователя.",
)
@inject
def get_all_by_cart_user(
    use_case: Annotated[
        UseCaseMultipleEntities,
        Depends(Provide[CartItemContainer.get_all_by_cart_user]),
    ],
    user_id: Annotated[int, Query(description="ID пользователя")],
) -> list[CartItemOutSchema]:
    """
    Получить все товары в корзине по user_id.

    - **user_id**: ID пользователя
    """
    try:
        return use_case.execute(user_id)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_all_by_cart_user", e)


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CartItemOutSchema,
    summary="Обновить количество товара в корзине",
    description="Обновляет количество указанного товара в корзине.",
)
@inject
def update_cart_item(
    cart_item: Annotated[
        CartItemServiceInterface,
        Depends(cart_by_id),
    ],
    data: CartItemUpdatePartialSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[CartItemContainer.update_item_in_cart_use_case]),
    ],
) -> CartItemOutSchema:
    """
    Обновить элемент корзины.

    - **id**: ID элемента корзины (в path)
    - **item_id**: ID товара (в теле запроса)
    - **quantity**: Новое количество (в теле запроса)
    """
    try:
        return use_case.execute(
            cart_item=cart_item,
            item_id=data.item_id,
            quantity=data.quantity,
        )
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in update_cart_item", e)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить товар из корзины",
    description="Удаляет указанный товар из корзины пользователя.",
)
@inject
def delete_cart_item(
    cart_item: Annotated[
        CartItemServiceInterface,
        Depends(cart_by_id),
    ],
    item_id: Annotated[int, Query(description="ID удаляемого товара")],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[CartItemContainer.delete_item_in_cart_use_case]),
    ],
) -> None:
    """
    Удалить товар из корзины пользователя.

    - **id**: ID корзины (в path)
    - **item_id**: ID товара (в query)
    """
    try:
        use_case.execute(
            cart_item=cart_item,
            item_id=item_id,
        )
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in delete_cart_item", e)
