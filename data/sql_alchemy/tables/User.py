from typing import Optional, List

from sqlalchemy import Integer, VARCHAR, Boolean
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship


class User(DeclarativeBase):
    # todo type limits at least for VARCHAR and/or default values
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
    active: Mapped[bool] = mapped_column(Boolean)
    images: Mapped[List["Image"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id}, chat_id={self.chat_id}, first_name={self.first_name}"
