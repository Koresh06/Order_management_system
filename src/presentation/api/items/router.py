from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status
from dependency_injector.wiring import Provide, inject

from src.application.containers.container import Container
from src.application.services.items.item_service_interface import ItemServiceInterface
from src.presentation.api.items.schemas import ItemCreateSchema, ItemOutSchema

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=ItemOutSchema, status_code=status.HTTP_201_CREATED)
@inject
async def create_item(
    item: ItemCreateSchema,
    service: Annotated[
        ItemServiceInterface,
        Depends(Provide[Container.item_service]),
    ],
) -> ItemOutSchema:
    try:
        return service.create(item)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/", response_model=list[ItemOutSchema], status_code=status.HTTP_200_OK)
@inject
async def get_all_items(
    service: Annotated[
        ItemServiceInterface,
        Depends(Provide[Container.item_service]),
    ],
) -> list[ItemOutSchema]:
    return service.get_all()


@router.get("/user/{id}", response_model=list[ItemOutSchema], status_code=status.HTTP_200_OK)
@inject
async def get_all_items_by_user(
    id: Annotated[int, Path],
    service: Annotated[
        ItemServiceInterface,
        Depends(Provide[Container.item_service]),
    ],
) -> list[ItemOutSchema]:
    try:
        service.get_all_by_user(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))