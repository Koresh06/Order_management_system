from typing import Annotated
from dependency_injector.wiring import Provide, inject

from fastapi import Path, Depends, HTTPException, status

from src.application.containers.container import Container
from src.domain.entitys.product import ProductModel
from src.application.use_cases.base_use_case import BaseUseCase


@inject
def product_by_id(
    id: Annotated[int, Path],
    products_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.products_use_case]),
    ],
) -> ProductModel:
    product = products_use_case.get_by_id(id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {id} not found!",
    )
