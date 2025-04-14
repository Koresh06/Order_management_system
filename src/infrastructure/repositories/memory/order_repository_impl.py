from src.domain.repositories.order_repository_intarface import OrderRepositoryInterface
from src.domain.entitys.order import OrderModel
from src.domain.entitys.cart_item import CartItemModel


class OrderRepositoryImpl(OrderRepositoryInterface):
    def __init__(self):
        self.orders = []
        self.counter = 1

    def create(
        self,
        user_id: int,
        items: CartItemModel,
        total_price: float,
    ) -> OrderModel:
        new_order = OrderModel(
            id=self.counter,
            user_id=user_id,
            items=[items],
            total_price=total_price
        )
        self.orders.append(new_order)
        self.counter += 1
        return new_order

    def get_by_id(self, order_id: int) -> OrderModel:
        for order in self.orders:
            if order.id == order_id:
                return order
            

    def get_all_orders_by_user(self, user_id: int) -> list[OrderModel]:
        orders = []
        for order in self.orders:
            if order.user_id == user_id:
                orders.append(order)
        return orders
    

    def get_all(self) -> list[OrderModel]:
        return self.orders
        
    
    def delete(self, order_id: int) -> None:
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)