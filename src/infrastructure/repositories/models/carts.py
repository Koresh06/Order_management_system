from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import Product, User


class Cart(Base):
    __tablename__ = "carts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
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

    user_rel: Mapped["User"] = relationship(
        "User",
        back_populates="cart_rel",
    )
    product_rel: Mapped[List["Product"]] = relationship(
        "Product",
        back_populates="cart_rel",
    )

    def __repr__(self) -> str:
        return f"Cart(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, quantity={self.quantity})"
