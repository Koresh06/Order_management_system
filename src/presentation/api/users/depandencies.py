import uuid
from typing import Annotated
from dependency_injector.wiring import Provide, inject

from fastapi import Path, Depends, HTTPException, status

from src.application.containers.container import Container
from src.domain.entitys.user import UserModel
from src.application.use_cases.intarfase.users_use_case import UsersUseCaseABC


@inject
def user_by_id(
    id: Annotated[int, Path],
    users_use_case: Annotated[
        UsersUseCaseABC,
        Depends(Provide[Container.users_use_case]),
    ],
) -> UserModel:
    user = users_use_case.get_by_id(id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {int} not found!",
    )
