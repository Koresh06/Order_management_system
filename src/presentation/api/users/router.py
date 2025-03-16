from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import inject, Provide

from src.application.containers.container import Container
from src.application.use_cases.intarfase.users_use_case import UsersUseCaseABC
from src.presentation.api.users.schemas import UserCreateSchema, UserOutSchema


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
    users_use_case: UsersUseCaseABC = Depends(Provide[Container.users_use_case]),
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
    users_use_case: UsersUseCaseABC = Depends(Provide[Container.users_use_case]),
):
    user = users_use_case.create(user_create)
    return UserOutSchema.model_validate(user)
