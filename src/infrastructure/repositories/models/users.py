from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, String, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base

if TYPE_CHECKING:
    from src.infrastructure.repositories.models import Order, Product, Payment, Role


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.id"),
        nullable=True,
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
    )
    email: Mapped[str] = mapped_column(String(120))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )

    roles_rel: Mapped["Role"] = relationship(
        "Role",
        back_populates="users_rel",
    )
    products_rel: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="users_rel",
        cascade="all, delete",
    )
    orders_rel: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="users_rel",
        cascade="all, delete",
    )
    payments_rel: Mapped[list["Payment"]] = relationship(
        "Payment",
        back_populates="users_rel",
        cascade="all, delete",
    )

    def __repr__(self):
        return super().__repr__(
            f"User(id={self.id}, name={self.username}, email={self.email}, created_at={self.created_at}, updated_at={self.updated_at})"
        )
