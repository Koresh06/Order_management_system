from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from src.application.containers.container import Container
from src.presentation.api.products.schemas import (
    ProductCreateSchema,
    ProductOutSchema,
    ProductUpdateSchema,
    ProductUpdatePartilSchema,
)
from src.application.use_cases.base_use_case import BaseUseCase
from src.presentation.api.products.depandencies import product_by_id


router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductOutSchema,
)
@inject
def create_product(
    product_create: ProductCreateSchema,
    products_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.products_use_case]),
    ],
) -> ProductOutSchema:
    product = products_use_case.create(product_create)
    return ProductOutSchema.model_validate(product)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[ProductOutSchema],
)
@inject
def get_products(
    products_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.products_use_case]),
    ],
) -> list[ProductOutSchema]:
    products = products_use_case.get_all()
    return [ProductOutSchema.model_validate(product) for product in products]


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOutSchema,
)
@inject
def get_product_by_id(
    product: Annotated[
        ProductOutSchema,
        Depends(product_by_id),
    ],
) -> ProductOutSchema:
    return ProductOutSchema.model_validate(product)


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOutSchema,
)
@inject
def replace_product(
    product_update: ProductUpdateSchema,
    product: Annotated[
        ProductOutSchema,
        Depends(product_by_id),
    ],
    products_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.products_use_case]),
    ],
) -> ProductOutSchema:
    product = products_use_case.update(
        product,
        product_update,
    )
    return ProductOutSchema.model_validate(product)


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOutSchema,
)
@inject
def modify_product(
    product_update: ProductUpdatePartilSchema,
    product: Annotated[
        ProductOutSchema,
        Depends(product_by_id),
    ],
    products_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.products_use_case]),
    ],
) -> ProductOutSchema:
    product = products_use_case.update(
        product,
        product_update,
        partial=True,
    )
    return ProductOutSchema.model_validate(product)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
def delete_product(
    product: Annotated[
        ProductOutSchema,
        Depends(product_by_id),
    ],
    products_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.products_use_case]),
    ],
) -> None:
    products_use_case.delete(product.id)