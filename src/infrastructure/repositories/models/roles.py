from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.infrastructure.repositories.models import Base


if TYPE_CHECKING:
    from src.infrastructure.repositories.models import User


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
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

    users_rel: Mapped[list["User"]] = relationship(
        "User",
        back_populates="roles_rel",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return super().__repr__(
            f"Role(id={self.id}, name={self.name}, created_at={self.created_at}, updated_at={self.update_at})"
        )
