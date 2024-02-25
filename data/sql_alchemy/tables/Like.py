from typing import Optional

from sqlalchemy import Integer, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from data.sql_alchemy.tables.Base import Base
from data.sql_alchemy.tables.User import User


class Like(Base):
    __tablename__ = "like"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    superior: Mapped["User"] = relationship(back_populates="relateToSuperior")
    interior: Mapped["User"] = relationship(back_populates="relateToInterior")
    is_executed: Mapped[bool] = mapped_column(Boolean)
    is_mutual: Mapped[Optional[bool]] = mapped_column(Boolean)

    def __repr__(self):
        return f"Like(id={self.id}, superior={self.superior.__repr__()}, interior={self.interior.__repr__()}, is_executed={self.is_executed}, is_mutual={self.is_mutual})"

