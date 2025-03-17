from src.application.services.base_service import BaseService
from src.domain.entitys.order import OrderModel
from src.domain.repositories.base_repository import BaseRepository


class OrdersServiceImpl(BaseService):
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    def create(self, order: OrderModel) -> OrderModel:
        return self._repository.create(order)

    def get_all(self) -> list[OrderModel]:
        return self._repository.get_all()

    def get_by_id(self, id: int) -> OrderModel:
        return self._repository.get_by_id(id)

    def update(
        self,
        order: OrderModel,
        order_update: OrderModel,
        partial: bool = False,
    ) -> OrderModel:
        return self._repository.update(
            order=order,
            order_update=order_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._repository.delete(id)
