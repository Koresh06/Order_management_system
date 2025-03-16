from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, ForeignKey, func, Float
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import Enum as SQLAlchemyEnum

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import Order, User


class StatusEnum(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class Payment(Base):
    __tablename__ = "payments"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
    )
    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("orders.id"),
    )
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[bool] = mapped_column(
        SQLAlchemyEnum(StatusEnum),
        default=StatusEnum.PENDING.value,
        server_default=StatusEnum.PENDING.value,
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

    users_rel: Mapped["User"] = relationship(
        "User",
        back_populates="payments_rel",
    )
    orders_rel: Mapped["Order"] = relationship(
        "Order",
        back_populates="payments_rel",
    )

    def __repr__(self):
        return super().__repr__(
            f"Payment(id={self.id}, user_id={self.user_id}, order_id={self.order_id}, amount={self.amount}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at})",
        )
