from typing import Optional, List

from sqlalchemy import Integer, VARCHAR, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Image(Base):
    # todo type limits at least for VARCHAR and/or default values
    __tablename__ = "image"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    photo: Mapped[str] = mapped_column(VARCHAR)
    user: Mapped["User"] = relationship(back_populates="belongsTo")

    def __repr__(self) -> str:
        return f"Image(id={self.id}, photo={self.photo})"


class Like(Base):
    __tablename__ = "like"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    superior: Mapped["User"] = relationship(back_populates="user")
    interior: Mapped["User"] = relationship(back_populates="user")
    is_executed: Mapped[bool] = mapped_column(Boolean)
    is_mutual: Mapped[Optional[bool]] = mapped_column(Boolean)

    def __repr__(self):
        return f"Like(id={self.id}, superior={self.superior.__repr__()}, interior={self.interior.__repr__()}, is_executed={self.is_executed}, is_mutual={self.is_mutual})"


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
    images: Mapped[Optional[List["Image"]]] = relationship(back_populates="image", cascade=USER_CASCADE_MODE)
    likes_as_superior: Mapped[Optional[List["Like"]]] = relationship(back_populates="like", cascade=USER_CASCADE_MODE)
    like_as_interior: Mapped[Optional[List["Like"]]] = relationship(back_populates="like", cascade=USER_CASCADE_MODE)

    def __repr__(self):
        return f"User(id={self.id}, chat_id={self.chat_id}, first_name={self.first_name}"