from sqlalchemy import Integer, VARCHAR
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Image(DeclarativeBase):
    # todo type limits at least for VARCHAR and/or default values
    __tablename__ = "image"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    photo: Mapped[str] = mapped_column(VARCHAR)
