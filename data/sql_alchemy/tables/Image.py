from sqlalchemy import Integer, VARCHAR
from sqlalchemy.orm import mapped_column, Mapped, relationship

from data.sql_alchemy.tables.Base import Base
from data.sql_alchemy.tables.User import User


class Image(Base):
    # todo type limits at least for VARCHAR and/or default values
    __tablename__ = "image"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    photo: Mapped[str] = mapped_column(VARCHAR)
    user: Mapped["User"] = relationship(back_populates="shows")

    def __repr__(self) -> str:
        return f"Image(id={self.id}, photo={self.photo})"

