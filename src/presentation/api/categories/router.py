from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from src.domain.use_case.intarface import UseCaseOneEntity
from src.application.containers.category_container import CategoryContainer
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.presentation.api.categories.schemas import CategoryCreateSchema, CategoryOutSchema

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    response_model=CategoryOutSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Создать категорию",
    description="Создает новую категорию.",
)
@inject
def create_category(
    category: CategoryCreateSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[CategoryContainer.create_category_use_case]),
    ],
) -> CategoryOutSchema:
    try:
        return use_case.execute(category)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in create_category", e)


# @router.get(
#     "/",
#     response_model=list[CategoryOutSchema],
#     status_code=status.HTTP_200_OK,
# )
# @inject
# def get_all_categories(
#     service: Annotated[
#         CategoryServiceInterface,
#         Depends(Provide[Container.category_service]),
#     ],
# ) -> list[CategoryOutSchema]:
#     return service.get_all()
