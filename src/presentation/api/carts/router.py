from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import Field
from dependency_injector.wiring import Provide, inject

from src.application.containers.container import Container
from src.application.services.cart_item.cart_item_service_intarface import CartItemServiceInterface
from src.presentation.api.carts.depandencies import cart_by_id
from src.presentation.api.carts.schemas import (
    CartItemOutSchema,
    CartItemCreateSchema,
    CartItemUpdateSchema,
    CartItemUpdatePartialSchema,
)


router = APIRouter(
    prefix="/carts",
    tags=["carts"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CartItemOutSchema,
)
@inject
async def add_cart_item(
    cart_item: CartItemCreateSchema,
    service: Annotated[
        CartItemServiceInterface,
        Depends(Provide[Container.cart_item_service]),
    ],
) -> CartItemOutSchema:
    try:
        return service.add_item(cart_item)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CartItemOutSchema],
)
@inject
async def get_all_carts(
    service: Annotated[
        CartItemServiceInterface,
        Depends(Provide[Container.cart_item_service]),
    ],
) -> list[CartItemOutSchema]:
    return service.get_all()


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CartItemOutSchema,
)
@inject
async def update_cart_item(
    cart_item: Annotated[
        CartItemServiceInterface,
        Depends(cart_by_id),
    ],
    data: CartItemUpdatePartialSchema,
    service: Annotated[
        CartItemServiceInterface,
        Depends(Provide[Container.cart_item_service]),
    ],
) -> CartItemOutSchema:
    try:
        return service.update_cart_quantity(
            cart_item=cart_item,
            item_id=data.item_id,
            quantity=data.quantity,
        )
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
async def delete_cart_item(
    cart_item: Annotated[
        CartItemServiceInterface,
        Depends(cart_by_id),
    ],
    item_id: int,
    service: Annotated[
        CartItemServiceInterface,
        Depends(Provide[Container.cart_item_service]),
    ],
) -> None:
    try:
        service.delete_cart_item(cart_item=cart_item, item_id=item_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))