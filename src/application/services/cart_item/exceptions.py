from src.domain.exceptions.api_exception import ApiException


class CartItemAlreadyExistsError(ApiException):
    pass


class UserNotFoundError(ApiException):
    pass


class ItemNotFoundError(ApiException):
    pass