import uuid

from src.domain.exceptions.users import UserAlreadyExistsError
from src.domain.repositories.user_repository_intarface import UserRepositoryInterface
from src.domain.services.user.security_intarface import PasswordHasherInterface
from src.domain.services.user.send_email_intarface import EmailServiceInterface
from src.domain.services.user.user_service_interface import UserServiceInterface
from src.domain.entitys.user import UserModel


class UserService(UserServiceInterface):
    def __init__(
        self,
        user_repo: UserRepositoryInterface,
        password_hasher: PasswordHasherInterface,
        email_service: EmailServiceInterface,
    ):
        self.user_repo = user_repo
        self.password_hasher = password_hasher
        self.email_service = email_service

    def create_user(self, user: UserModel) -> UserModel:
        existing_user = self.user_repo.get_by_email(user.email)
        if existing_user:
            raise UserAlreadyExistsError("A user with this email already exists")
        
        hashed_password = self.password_hasher.hash(user.password)
        user.password = hashed_password

        created_user = self.user_repo.create(user)

        verification_token = uuid.uuid4().hex 
        self.email_service.send_verification_email(user.email, verification_token)

        return created_user

    def get_all(self, limit: int, offset: int) -> list[UserModel]:
        return self.user_repo.get_all(limit, offset)
    
    def get_by_id(self, id: int) -> UserModel:
        return self.user_repo.get_by_id(id)
    
    def delete(self, id: int) -> bool:
        return self.user_repo.delete(id)