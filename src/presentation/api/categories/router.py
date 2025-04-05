from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, status
from dependency_injector.wiring import Provide, inject

from src.application.services.categories.category_service_intarface import CategoryServiceInterface
from src.presentation.api.categories.schemas import (
    CategoryCreateSchema,
    CategoryOutSchema,
    CategoryUpdatePartialSchema,
    CategoryUpdateSchema,
)


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)


# @router.post(
#     "/",
#     response_model=CategoryOutSchema,
#     status_code=status.HTTP_201_CREATED,
# )
# @inject
# async def create_category(
#     category: CategoryCreateSchema,
#     service: Annotated[
#         CategoryServiceInterface,
#         Depends(Provide[Container.category_service]),
#     ],
# ) -> CategoryOutSchema:
#     try:
#         return service.create(category)
#     except Exception as e:
#         raise HTTPException(status_code=404, detail=str(e))


# @router.get(
#     "/",
#     response_model=list[CategoryOutSchema],
#     status_code=status.HTTP_200_OK,
# )
# @inject
# async def get_all_categories(
#     service: Annotated[
#         CategoryServiceInterface,
#         Depends(Provide[Container.category_service]),
#     ],
# ) -> list[CategoryOutSchema]:
#     return service.get_all()
