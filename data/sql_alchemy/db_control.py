from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.sql_alchemy.tables.Base import Base

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Base.metadata.create_all(engine)
session = Session(engine)
