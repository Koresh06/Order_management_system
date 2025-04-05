from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from src.domain.services.user.user_service_interface import UserServiceInterface
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.domain.services.item.item_service_interface import ItemServiceInterface
from src.presentation.api.users.depandencies import user_by_id
from src.presentation.api.items.schemas import ItemCreateSchema, ItemOutSchema, GetAllByUserSchema
from src.application.containers.item_container import ItemContainer

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    response_model=ItemOutSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Создать новый товар",
    description="Создает новый товар и добавляет его в базу данных.",
)
@inject
def create_item(
    item: ItemCreateSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[ItemContainer.create_item_use_case]),
    ],
) -> ItemOutSchema:
    try:
        return use_case.execute(item)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in create_item", e)


@router.get(
    "/",
    response_model=list[ItemOutSchema],
    status_code=status.HTTP_200_OK,
    summary="Получить все товары",
    description="Возвращает список всех товаров в базе данных.",
)
@inject
def get_all_items(
    use_case: Annotated[
        UseCaseMultipleEntities,
        Depends(Provide[ItemContainer.get_all_items_use_case]),
    ],
) -> list[ItemOutSchema]:
    try:
        return use_case.execute()
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_all_items", e)


@router.get(
    "/{user_id}",
    response_model=GetAllByUserSchema,
    status_code=status.HTTP_200_OK,
    summary="Получить все товары по пользователю",
    description="Возвращает все товары, связанные с указанным пользователем.",
)
@inject
def get_all_items_by_user(
    user: Annotated[
        UserServiceInterface,
        Depends(user_by_id),
    ],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[ItemContainer.get_all_items_by_user_use_case]),
    ],
) -> GetAllByUserSchema:
    try:
        return use_case.execute(user)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_all_items_by_user", e)
