from fastapi import Path, Depends, HTTPException, status
from typing import Annotated
from dependency_injector.wiring import Provide, inject

from src.application.containers.main_container import MainContainer
from src.domain.services.user.user_service_interface import UserServiceInterface
from src.domain.entitys.user import UserModel


@inject
def user_by_id(
    user_id: Annotated[
        int,
        Path(
            title="User ID",
            description="Идентификатор пользователя",
            ge=1,
        )
    ],
    service: Annotated[
        UserServiceInterface,
        Depends(Provide[MainContainer.user_service])
    ],
) -> UserModel:
    """
    Получить пользователя по ID. Используется как зависимость.

    - **user_id**: ID пользователя
    """
    user = service.get_by_id(user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Пользователь с ID {user_id} не найден.",
    )
