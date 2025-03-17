from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, String, ForeignKey, Float, func, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base

if TYPE_CHECKING:
    from src.infrastructure.repositories.models import User, Cart


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
    )
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(
        Text,
        nullable=True,
        default="",
        server_default="",
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
        back_populates="products_rel",
    )
    cart_rel: Mapped["Cart"] = relationship(
        "Cart",
        back_populates="products_rel",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return super().__repr__(
            f"Product(id={self.id}, name={self.name}, price={self.price}, created_at={self.created_at}, updated_at={self.updated_at})"
        )
