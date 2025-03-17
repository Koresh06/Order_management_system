from src.application.services.base_service import BaseService
from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.entitys.order import OrderModel


class OrdersUseCaseImpl(BaseUseCase):
    def __init__(self, service: BaseService):
        self._service = service

    def create(self, order: OrderModel) -> OrderModel:
        return self._service.create(order)

    def get_all(self) -> list[OrderModel]:
        return self._service.get_all()

    def get_by_id(self, id: int) -> OrderModel:
        return self._service.get_by_id(id)

    def update(
        self,
        order: OrderModel,
        order_update: OrderModel,
        partial: bool = False,
    ) -> OrderModel:
        return self._service.update(
            order=order,
            order_update=order_update,
            partial=partial,
        )

    def delete(self, id: int) -> None:
        return self._service.delete(id)
