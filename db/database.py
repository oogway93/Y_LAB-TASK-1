from typing import Annotated

from sqlalchemy import String
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

from config import async_link

async_engine = create_async_engine(async_link, echo=True)

async_session = async_sessionmaker(async_engine)

str_256 = Annotated[str, String(256)]


class Base(DeclarativeBase):
    """Declarative Base Class."""
    pass