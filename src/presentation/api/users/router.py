from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import Provide, inject
from src.application.containers.user_container import UserContainer
from src.domain.services.user.user_service_interface import UserServiceInterface
from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.presentation.api.users.depandencies import user_by_id
from src.presentation.api.users.schemas import (
    PaginationQueryParams,
    UserCreateSchema,
    UserOutSchema,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Пользователь не найден"}},
)


@router.post(
    "/",
    response_model=UserOutSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Создать пользователя",
    description="Создает нового пользователя в системе.",
)
@inject
def create_user(
    user: UserCreateSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[UserContainer.register_user_use_case]),
    ],
) -> UserOutSchema:
    """
    Создание нового пользователя.

    - **name**: Имя пользователя
    - **email**: Электронная почта
    - **password**: Пароль
    """
    try:
        return use_case.execute(user)
    except Exception as e:
        raise ApiErrorHandling.http_error("Ошибка при создании пользователя", e)


@router.get(
    "/",
    response_model=list[UserOutSchema],
    status_code=status.HTTP_200_OK,
    summary="Получить список пользователей",
    description="Возвращает список всех пользователей с пагинацией.",
)
@inject
async def get_all_users(
    use_case: Annotated[
        UseCaseMultipleEntities,
        Depends(Provide[UserContainer.get_all_users_use_case]),
    ],
    pagination: Annotated[PaginationQueryParams, Depends()],
) -> list[UserOutSchema]:
    """
    Получение списка пользователей с пагинацией.

    - **pagination.limit**: Количество пользователей на странице (по умолчанию 10)
    - **pagination.offset**: Смещение от начала списка пользователей
    """

    return use_case.execute(pagination.limit, pagination.offset)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Удалить пользователя",
    description="Удаляет пользователя по его ID.",
)
@inject
async def delete_user(
    user: Annotated[
        UserServiceInterface,
        Depends(user_by_id),
    ],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[UserContainer.delete_user_use_case]),
    ],
) -> None:
    """
    Удалить пользователя по ID.

    - **user_id**: Идентификатор пользователя
    """
    try:
        use_case.execute(user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Пользователь не найден: {e}")
