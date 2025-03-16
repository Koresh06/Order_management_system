from sqlalchemy import select
from src.domain.repositories.base_repository import BaseRepository
from src.infrastructure.repositories.sqlite.settings.db_helper import SQLiteDatabaseHelper
from src.infrastructure.repositories.models import Order
from src.presentation.api.orders.schemas import OrderCreateSchema


class SQLiteOrdersRepositoryImpl(BaseRepository):
    def __init__(self, db_helper: SQLiteDatabaseHelper):
        self.db_helper = db_helper

    def create(self, order: OrderCreateSchema) -> Order:
        with self.db_helper.get_session() as session:
            create_order = Order(
                user_id=order.user_id,
                status=order.status,
                total_price=order.total_price,
            )
            session.add(create_order)
            session.commit()
            session.refresh(create_order)
            return create_order

    def get_all(self) -> list[Order]:
        with self.db_helper.get_session() as session:
            return session.scalars(select(Order)).all()
        

    def get_by_id(self, id: int) -> Order:
        with self.db_helper.get_session() as session:
            return session.get(Order, id)
        
        
    def update(
        self,
        order: Order,
        order_update: dict,
        partial: bool = False,
    ) -> Order:
        with self.db_helper.get_session() as session:
            order_from_db = session.get(Order, order.id)
            for key, value in order_update.model_dump(exclude_unset=partial).items():
                setattr(order_from_db, key, value)
            session.commit()
            session.refresh(order_from_db)
            return order_from_db

    def delete(self, id: int) -> None:
        with self.db_helper.get_session() as session:
            order = session.get(Order, id)
            session.delete(order)
            session.commit()
        
    