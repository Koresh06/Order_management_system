from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import Product, Cart

class CartProduct(Base):
    __tablename__ = "cart_products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    cart_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("carts.id"),
        nullable=False,
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
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

    cart_rel: Mapped["Cart"] = relationship(
        "Cart",
        back_populates="cart_products_rel",
    )
    product_rel: Mapped["Product"] = relationship(
        "Product",
        back_populates="cart_products_rel",
    )

    def __repr__(self) -> str:
        return f"CartProduct(id={self.id}, cart_id={self.cart_id}, product_id={self.product_id}, quantity={self.quantity})"