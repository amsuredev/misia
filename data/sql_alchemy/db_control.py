from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session

from data.sql_alchemy.tables.tables import Base


def __create_db() -> Engine:
    engine = create_engine("sqlite:///misia.db", echo=True)
    Base.metadata.create_all(engine)
    return engine


def get_db_session() -> Session:
    return Session(__create_db())
