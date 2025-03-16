from datetime import datetime
from src.domain.repositories.base_repository import BaseRepository
from src.domain.entitys.order import OrderModel


class MemoryOrdersRepositoryImpl(BaseRepository):
    def __init__(self):
        self.orders = []
        self.counter = 0

    def create(self, order: OrderModel) -> OrderModel:
        self.counter += 1
        new_order = OrderModel(
            id=self.counter,
            order_id=order.order_id,
            prduct_id=order.prduct_id,
            status=order.status,
            total_price=order.total_price,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        self.orders.append(new_order)
        return new_order

    def get_all(self) -> list[OrderModel]:
        return self.orders

    def get_by_id(self, id: int) -> OrderModel:
        for order in self.orders:
            if order.id == id:
                return order
        return None

    def update(
        self,
        order: OrderModel,
        order_update: OrderModel,
        partial: bool = False,
    ) -> OrderModel:
        for index, item in enumerate(self.orders):
            if item.id == order.id:
                for key, value in order_update.model_dump(exclude_unset=partial).items():
                    setattr(item, key, value)
                self.orders[index] = item
                return item
        return None

    def delete(self, id: int) -> None:
        for order in self.orders:
            if order.id == id:
                self.orders.remove(order)
                return None
