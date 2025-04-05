from src.application.utils.error_handlers_utils import ErrorHandlingUtils
from src.domain.entitys.user import UserModel
from src.domain.use_case.intarface import UseCaseMultipleEntities, UseCaseOneEntity


from src.domain.services.user.user_service_interface import UserServiceInterface


class RegisterUserUseCase(UseCaseOneEntity):
    def __init__(
        self,
        service: UserServiceInterface,
    ) -> None:
        self.service = service  

    def execute(self, user: UserModel) -> UserModel:
        try:
            return self.service.create_user(user)
        except Exception as exec:
            raise ErrorHandlingUtils.application_error("Error in RegisterUserUseCase", exec)


class GetAllUsersUseCase(UseCaseMultipleEntities):
    def __init__(
        self, 
        service: UserServiceInterface
    ) -> None:
        self.service = service
        
    try:
        def execute(self, limit: int, offset: int) -> list[UserModel]:
            return self.service.get_all(limit, offset)
    except Exception as e:
        raise ErrorHandlingUtils.application_error("Error in GetAllUsersUseCase", e)
    