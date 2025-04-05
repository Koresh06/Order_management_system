from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status
from dependency_injector.wiring import Provide, inject

from src.presentation.api.api_error_handling import ApiErrorHandling
from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.domain.services.item.item_service_interface import ItemServiceInterface
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
    "/{id}",
    response_model=GetAllByUserSchema,
    status_code=status.HTTP_200_OK,
)
@inject
def get_all_items_by_user(
    id: Annotated[int, Path],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[ItemContainer.get_all_items_by_user_use_case]),
    ],
) -> GetAllByUserSchema:
    try:
        return use_case.execute(id)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in get_all_items_by_user", e)
