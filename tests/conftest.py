import pytest
from unittest.mock import MagicMock
from src.application.containers.user_container import UserContainer
from src.application.services.users.user_service import UserService
from src.domain.entitys.user import UserModel


@pytest.fixture
def mock_user_model():
    return UserModel(
        id=1,
        username="testuser",
        email="test@example.com",
        full_name="Test User",
        password="123456"
    )

@pytest.fixture
def user_container_with_mocks():
    container = UserContainer()

    container.user_repo.override(MagicMock())
    container.user_service.override(MagicMock())
    container.password_hasher.override(MagicMock())
    container.email_service.override(MagicMock())

    yield container

    container.unwire()
