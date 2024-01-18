from typing import List, Annotated

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

metadata_obj = MetaData()
intpk = Annotated[int, mapped_column(primary_key=True)]


class Menu(Base):
    __tablename__ = "menus"
    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    submenus_count: Mapped[int] = mapped_column(default=0, nullable=True)

    # submenu: Mapped[List["Submenu"]] = relationship(back_populates="menu", cascade="delete")


class Submenu(Base):
    __tablename__ = 'submenus'
    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    dishes_count: Mapped[int] = mapped_column(default=0)

    menu_id: Mapped[int] = mapped_column(ForeignKey("menus.id", ondelete="CASCADE"))
    menu: Mapped["Menu"] = relationship(back_populates="submenus")
    # dishes: Mapped["Dish"] = relationship(back_populates="submenus", cascade="all, delete")


class Dish(Base):
    __tablename__ = "dishes"
    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    price: Mapped[float] = mapped_column(index=True)

    submenu_id: Mapped[int] = mapped_column(ForeignKey("submenus.id", ondelete="CASCADE"))
    submenu: Mapped["Submenu"] = relationship(back_populates="dishes")


Menu.submenus = relationship('Submenu', back_populates='menu')
Submenu.dishes = relationship('Dish', back_populates='submenu')
