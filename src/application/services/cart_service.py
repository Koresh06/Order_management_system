from src.application.services.base_service import BaseService
from src.domain.entitys.cart import CartModel
from src.domain.repositories.base_repository import BaseRepository


class CartServiceImpl(BaseService):
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def create(self, cart: CartModel) -> CartModel:
        return self._repository.create(cart)

    def get_all(self) -> list[CartModel]:
        return self._repository.get_all()

    def get_by_id(self, id: int) -> CartModel:
        return self._repository.get_by_id(id)

    def update(
        self,
        cart: CartModel,
        cart_update: CartModel,
        partial: bool = False,
    ) -> CartModel:
        return self._repository.update(
            cart=cart,
            cart_update=cart_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._repository.delete(id)
