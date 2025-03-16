from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, String, ForeignKey, Float, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import User, Payment, OrderProduct


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
    )
    status: Mapped[str] = mapped_column(String(50))
    total_price: Mapped[float] = mapped_column(Float)
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
        back_populates="orders",
    )
    product_rel: Mapped["OrderProduct"] = relationship(
        "OrderProduct",
        back_populates="order_rel",
    )
    payment_rel: Mapped["Payment"] = relationship(
        "Payment",
        back_populates="order",
        cascade="all, delete",
    )

    def __repr__(self):
        return super().__repr__(
            f"Order(id={self.id}, user_id={self.user_id}, status={self.status}, total_price={self.total_price}, created_at={self.created_at}, updated_at={self.updated_at})"
        )
