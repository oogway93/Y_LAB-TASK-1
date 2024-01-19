from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import async_link

async_engine = create_async_engine(async_link, echo=True)

async_session = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
    """Declarative Base Class."""
    pass


