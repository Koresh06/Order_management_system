from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import Product, Order


class OrderProduct(Base):
    __tablename__ = "orders_products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("orders.id"),
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id"),
    )
    quantity: Mapped[int] = mapped_column(
        Integer,
        default=1,
        server_default="1",
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )

    order_rel: Mapped["Order"] = relationship(
        "Order",
        back_populates="products_rel",
    )
    product_rel: Mapped["Product"] = relationship(
        "Product",
        back_populates="orders_rel",
    )

    def __repr__(self) -> str:
        return f"OrderProduct(id={self.id}, order_id={self.order_id}, product_id={self.product_id})"
