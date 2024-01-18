from select import select

from db.database import async_engine, Base, async_session
from db.models import Menu


class AsyncORM:
    """ALL ORM METHODS."""

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def creation_menu(title: str, description: str, submenus_count: int):
        async with async_session() as session:
            menu = Menu(title=title, description=description, submenus_count=submenus_count)
            session.add(menu)
            await session.commit()

    @staticmethod
    async def getting_menu():
        async with async_session() as session:
            stmt = select(Menu)
            res = await session.execute(stmt)
            result = res.scalars().all()
            return result
