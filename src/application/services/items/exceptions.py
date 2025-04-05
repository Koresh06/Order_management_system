from src.domain.exceptions.api_exception import ApiException


class ItemAlreadyExistsError(ApiException):
    pass

class UserNotFoundError(ApiException):
    pass

class CategoryNotFoundError(ApiException):
    pass