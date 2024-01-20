import uuid
from typing import List, Annotated

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData, ForeignKey, Column, UUID
from sqlalchemy.orm import relationship

from db.database import Base

metadata_obj = MetaData()
# intpk = Annotated[uuid.UUID, mapped_column(primary_key=True, default=uuid.uuid4)]


class Menu(Base):
    __tablename__ = "menus"
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    # submenus_count: Mapped[int] = mapped_column(default=0)

    # submenu: Mapped[List["Submenu"]] = relationship(back_populates="menu", cascade="delete")


class Submenu(Base):
    __tablename__ = 'submenus'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    dishes_count: Mapped[int] = mapped_column(default=0)

    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id", ondelete="CASCADE"))
    menu: Mapped["Menu"] = relationship(back_populates="submenus")
    # dishes: Mapped["Dish"] = relationship(back_populates="submenus", cascade="all, delete")


class Dish(Base):
    __tablename__ = "dishes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())

    title: Mapped[str] = mapped_column(unique=True, nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    price: Mapped[float] = mapped_column(index=True)

    submenu_id: Mapped[int] = mapped_column(ForeignKey("submenus.id", ondelete="CASCADE"))
    submenu: Mapped["Submenu"] = relationship(back_populates="dishes")


Menu.submenus = relationship('Submenu', back_populates='menu')
Submenu.dishes = relationship('Dish', back_populates='submenu')
