from sqlalchemy import create_engine, Engine, URL
from sqlalchemy.orm import Session

from data.sql_alchemy.models import Base
from sqlalchemy_utils import database_exists, create_database
import os
from dotenv import load_dotenv

load_dotenv(".env")


def __get_engine() -> Engine:
    db_url = URL.create("postgresql+psycopg2",
                        username=os.getenv("USER"),
                        password=os.getenv("PASSWORD"),
                        host=os.getenv("HOST"),
                        database=os.getenv("DATABASE")
                        )
    engine = create_engine(db_url, echo=True)
    if not database_exists(db_url):
        create_database(db_url)
    Base.metadata.create_all(engine)
    return engine


def get_db_session() -> Session:
    return Session(__get_engine())
