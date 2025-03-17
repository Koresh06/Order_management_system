from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import DateTime, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import User, CartProduct


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
        unique=True, 
        nullable=False,
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
    cart_products_rel: Mapped[List["CartProduct"]] = relationship(
        "CartProduct",
        back_populates="cart_rel",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"Cart(id={self.id}, user_id={self.user_id})"