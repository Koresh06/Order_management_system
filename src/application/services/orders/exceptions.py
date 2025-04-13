from src.domain.exceptions.api_exception import ApiException


class CartItemNotFoundError(ApiException):
    pass


class OrderNotFoundError(ApiException):
    pass