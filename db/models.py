# import uuid
# from typing import List, Annotated
#
# from sqlalchemy.orm import Mapped, mapped_column
# from sqlalchemy import MetaData, ForeignKey, Integer, Column, UUID
# from sqlalchemy.orm import relationship
#
# from db.database import Base
#
# metadata_obj = MetaData()
#
#
# class Dish(Base):
#     __tablename__ = "dishes"
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
#     title: Mapped[str] = mapped_column(unique=True, nullable=True)
#     description: Mapped[str] = mapped_column(nullable=True)
#     price: Mapped[float] = mapped_column(index=True)
#     submenu_id = Column(UUID(as_uuid=True), ForeignKey("submenus.id", ondelete="CASCADE"))
#     submenus = relationship("Submenu", back_populates="dishes")
#
#
# class Submenu(Base):
#     __tablename__ = 'submenus'
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
#     title: Mapped[str] = mapped_column(unique=True)
#     description: Mapped[str]
#     menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id", ondelete="CASCADE"))
#     menu: Mapped["Menu"] = relationship(back_populates="submenus")
#     dishes = relationship('Dish', back_populates='submenus')
#
#
# class Menu(Base):
#     __tablename__ = "menus"
#     id = Column(
#         UUID(as_uuid=True),
#         primary_key=True,
#         default=uuid.uuid4,
#         index=True,
#         nullable=False,
#     )
#     title: Mapped[str] = mapped_column(unique=True)
#     description: Mapped[str]
#     submenus: Mapped["Submenu"] = relationship(back_populates='menu')

from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Menu(Base):
    __tablename__ = "menus"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        nullable=False,
    )
    title = Column(String)
    description = Column(String)
    submenus = relationship("Submenu", back_populates="menu", cascade="all, delete-orphan")


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        nullable=False,
    )
    title = Column(String)
    description = Column(String)
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id", ondelete="CASCADE"))
    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete-orphan")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        nullable=False,
    )
    title = Column(String, unique=True)
    description = Column(String)
    price = Column(Numeric)
    submenu_id = Column(
        UUID(as_uuid=True), ForeignKey("submenus.id", ondelete="CASCADE")
    )
    submenu = relationship("Submenu", back_populates="dishes")
