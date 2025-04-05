from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path, Query, status
from dependency_injector.wiring import Provide, inject
from pydantic import ValidationError

from src.application.containers.user_container import UserContainer
from src.domain.services.user.user_service_interface import UserServiceInterface
from src.domain.use_case.intarface import UseCaseOneEntity, UseCaseMultipleEntities
from src.presentation.api.api_error_handling import ApiErrorHandling
from src.presentation.api.users.schemas import (
    UserCreateSchema,
    UserOutSchema,
    UserUpdateSchema,
    UserUpdatePartialSchema,
)


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=UserOutSchema, status_code=status.HTTP_201_CREATED)
@inject
def create_user(
    user: UserCreateSchema,
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[UserContainer.register_user_use_case]),
    ],
) -> UserOutSchema:
    try:
        return use_case.execute(user)
    except Exception as e:
        raise ApiErrorHandling.http_error("Error in create_user", e)


@router.get("/", response_model=list[UserOutSchema])
@inject
async def get_all_users(
    use_case: Annotated[
        UseCaseMultipleEntities,
        Depends(Provide[UserContainer.get_all_users_use_case]),
    ],
    limit: int = Query(default=10),
    offset: int = Query(default=0),
) -> list[UserOutSchema]:
    return use_case.execute(limit, offset)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_user(
    id: Annotated[int, Path],
    use_case: Annotated[
        UseCaseOneEntity,
        Depends(Provide[UserContainer.delete_user_use_case]),
    ],
) -> None:
    try:
        use_case.execute(id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
