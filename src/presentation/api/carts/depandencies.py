from typing import Annotated
from dependency_injector.wiring import Provide, inject

from fastapi import Path, Depends, HTTPException, status

from src.application.services.cart_item.cart_item_service_intarface import CartItemServiceInterface
from src.domain.entitys.user import UserModel


# @inject
# def cart_by_id(
#     id: Annotated[int, Path],
#     service: Annotated[
#         CartItemServiceInterface,
#         Depends(Provide[Container.cart_item_service]),
#     ],
# ) -> UserModel:
#     try:
#         return service.get_by_cart(id)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))