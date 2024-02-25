from typing import Optional, List

from sqlalchemy import Integer, VARCHAR, Boolean
from sqlalchemy.orm import mapped_column, Mapped, relationship

from data.sql_alchemy.tables.Base import Base
from data.sql_alchemy.tables.Image import Image
from data.sql_alchemy.tables.Like import Like


class User(Base):
    # todo type limits at least for VARCHAR and/or default values
    USER_CASCADE_MODE = "all, delete-orphan"
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    chat_id: Mapped[str] = mapped_column(VARCHAR)
    first_name: Mapped[str] = mapped_column(VARCHAR)
    age: Mapped[int] = mapped_column(Integer)
    sex: Mapped[str] = mapped_column(VARCHAR)
    sex_preference: Mapped[str] = mapped_column(VARCHAR)
    profile_message: Mapped[Optional[str]]
    town: Mapped[str]
    country: Mapped[Optional[str]]
    is_active: Mapped[bool] = mapped_column(Boolean)
    images: Mapped[List["Image"]] = relationship(back_populates="user", cascade=USER_CASCADE_MODE)
    likes_as_superior: Mapped[List["Like"]] = relationship(back_populates="like", cascade=USER_CASCADE_MODE)
    like_as_interior: Mapped[List["Like"]] = relationship(back_populates="like", cascade=USER_CASCADE_MODE)

    def __repr__(self):
        return f"User(id={self.id}, chat_id={self.chat_id}, first_name={self.first_name}"
