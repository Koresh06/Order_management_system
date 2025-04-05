from passlib.context import CryptContext

from src.domain.services.user.security_intarface import PasswordHasherInterface


class PasswordHasher(PasswordHasherInterface):

    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["bcrypt"],
            deprecated="auto",
        )

    def hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify(self, password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(password, hashed_password)
