from src.domain.exceptions.api_exception import ApiException


class CategoryAlreadyExistsError(ApiException):
    pass

class UserNotFoundError(ApiException):
    pass