from src.domain.exceptions.api_exception import ApiException

class UserAlreadyExistsError(ApiException):
    """Исключение, если пользователь уже существует"""
    
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
