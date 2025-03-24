from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from dependency_injector.wiring import Provide, inject

from src.application.containers.container import Container
from src.application.services.users.user_service_interface import UserServiceInterface
from src.presentation.api.users.schemas import (
    UserCreateSchema,
    UserOutSchema,
    UserUpdateSchema,
    UserUpdatePartialSchema,
)


from src.application.services.users.user_service_impl import NotFoundRole


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserOutSchema, status_code=status.HTTP_201_CREATED)
@inject
async def create_user(
    user: UserCreateSchema,
    repo: Annotated[
        UserServiceInterface,
        Depends(Provide[Container.user_service]),
    ],
) -> UserOutSchema:
    try:
        return repo.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=list[UserOutSchema])
@inject
async def get_all_users(
    repo: Annotated[
        UserServiceInterface,
        Depends(Provide[Container.user_service]),
    ],
) -> list[UserOutSchema]:
    return repo.get_all()