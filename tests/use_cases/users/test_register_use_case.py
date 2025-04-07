from src.application.containers.user_container import UserContainer
from src.domain.use_case.intarface import UseCaseOneEntity
from src.domain.entitys.user import UserModel


def test_register_user_use_case_calls_service(
    user_container_with_mocks: UserContainer,
    mock_user_model: UserModel,
) -> None:
    user_container_with_mocks.user_service().create_user.return_value = mock_user_model
    use_case: UseCaseOneEntity = user_container_with_mocks.register_user_use_case()
    result = use_case.execute(mock_user_model)

    assert result == mock_user_model

    user_container_with_mocks.user_service().create_user.assert_called_once_with(mock_user_model)
