import uuid

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from db.database import async_engine, Base, engine, SessionLocal
from db.models import Menu
from db import schemas


class RestaurantService:
    """ALL ORM METHODS."""

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def creation_menu(data: schemas.Menu, db: Session):
        created_menu = Menu(title=data.title, description=data.description)
        db.add(created_menu)
        db.commit()
        db.refresh(created_menu)
        return created_menu

    @staticmethod
    def getting_list_menus(db: Session):
        return db.query(Menu).all()

    @staticmethod
    def getting_menu_by_id(id: uuid.UUID, db: Session):
        try:
            stmt = db.query(Menu).filter(Menu.id == id).first()
        except Exception as e:
            print(e)
            return False
        return stmt

    @staticmethod
    def updating_menu(id: uuid.UUID, data: schemas.Menu, db: Session):
        updated_menu = db.query(Menu).filter(Menu.id == id).first()
        updated_menu.title = data.title
        updated_menu.description = data.description
        db.add(updated_menu)
        db.commit()
        db.refresh(updated_menu)
        return updated_menu

    @staticmethod
    def delete_menu(id: uuid.UUID, db):
        deleted_menu = db.query(Menu).filter(Menu.id == id).first()
        db.delete(deleted_menu)
        db.commit()
