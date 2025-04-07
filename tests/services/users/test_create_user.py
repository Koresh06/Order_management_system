import pytest
from src.application.containers.user_container import UserContainer
from src.application.services.users.exceptions import UserAlreadyExistsError
from src.domain.services.user.user_service_interface import UserServiceInterface
from src.domain.entitys.user import UserModel

