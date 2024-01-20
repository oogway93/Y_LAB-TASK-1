from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import async_link, link

engine = create_engine(link)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)

async_engine = create_async_engine(async_link)
async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    """Declarative Base Class."""
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
