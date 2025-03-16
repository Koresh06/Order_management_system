from typing import Annotated
from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from src.application.containers.container import Container
from src.application.use_cases.base_use_case import BaseUseCase
from src.presentation.api.users.schemas import (
    UserCreateSchema,
    UserOutSchema,
    UserUpdateSchema,
    UserUpdatePartialSchema,
)
from src.presentation.api.users.depandencies import user_by_id


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[UserOutSchema],
)
@inject
def get_users(
    users_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.users_use_case]),
    ],
) -> list[UserOutSchema]:
    users = users_use_case.get_all()
    return [UserOutSchema.model_validate(user) for user in users]


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOutSchema,
)
@inject
def create_user(
    user_create: UserCreateSchema,
    users_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.users_use_case]),
    ],
):
    user = users_use_case.create(user_create)
    return UserOutSchema.model_validate(user)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOutSchema,
)
@inject
def get_user_by_id(
    user: Annotated[
        UserOutSchema,
        Depends(user_by_id),
    ]
) -> UserOutSchema:
    return UserOutSchema.model_validate(user)


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOutSchema,
)
@inject
def replace_user(
    user_update: UserUpdateSchema,
    user: Annotated[
        UserOutSchema,
        Depends(user_by_id),
    ],
    users_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.users_use_case]),
    ],
):
    user = users_use_case.update(
        user=user,
        user_update=user_update,
    )
    return UserOutSchema.model_validate(user)


@router.patch(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOutSchema,
)
@inject
def modify_user(
    user_update: UserUpdatePartialSchema,
    user: Annotated[
        UserOutSchema,
        Depends(user_by_id),
    ],
    users_use_case: Annotated[
        BaseUseCase,
        Depends(Provide[Container.users_use_case]),
    ],
):
    user = users_use_case.update(
        user=user,
        user_update=user_update,
        partial=True,
    )
    return UserOutSchema.model_validate(user)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
@inject
def delete_user(
    user: Annotated[
        UserOutSchema,
        Depends(user_by_id),
    ],
    users_use_case: Annotated[
        BaseUseCase,    
        Depends(Provide[Container.users_use_case]),
    ],
):
    users_use_case.delete(user.id)
    