from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from config import link

engine = create_engine(link)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    """Declarative Base Class."""
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
