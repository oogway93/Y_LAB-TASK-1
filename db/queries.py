import uuid

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from db.database import async_engine, Base, async_session
from db.models import Menu
from db import schemas


class AsyncORM:
    """ALL ORM METHODS."""

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def creation_menu(title: str, description: str):
        async with async_session() as session:
            menu = Menu(title=title, description=description)
            session.add(menu)
            await session.commit()

    @staticmethod
    async def getting_list_menu():
        async with async_session() as session:
            stmt = (select(Menu))
            res = await session.execute(stmt)
            result = res.scalars().all()
            result_orm = [
                schemas.MenuAddDTO.model_validate(row, from_attributes=True)
                for row in result
            ]
            return result_orm

    @staticmethod
    async def getting_menu_by_id(id: uuid.UUID, db: Session):
        try:
            menu = db.query(Menu).filter(Menu.id == id).first()
            # result_orm = [
            #     schemas.MenuAddDTO.model_validate(row, from_attributes=True)
            #     for row in result
            # ]
        except Exception as e:
            return False
        return menu

    @staticmethod
    async def updating_menu(id: uuid.UUID, title: str, description: str):
        async with async_session() as session:
            query = update(Menu).where(Menu.id == id).values(title=title, description=description)
            session.execute(query)
            await session.commit()

    @staticmethod
    async def delete_menu(id: uuid.UUID):
        async with async_session() as session:
            query = delete(Menu).where(Menu.id == id)
            session.execute(query)
            await session.commit()
