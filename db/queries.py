import uuid

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from db.database import async_engine, Base, engine, SessionLocal
from db.models import Menu, Submenu
from db import schemas


class CRUDRestaurantService:
    """ALL ORM METHODS."""

    def __init__(self, model):
        self.model = model

    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def creation_menu(self, data: schemas.Menu | schemas.Submenu, db: Session):
        created_item = self.model(title=data.title, description=data.description)
        db.add(created_item)
        db.commit()
        db.refresh(created_item)
        return created_item

    def getting_list_menus(self, db: Session):
        return db.query(self.model).all()

    def getting_menu_by_id(self, id: uuid.UUID, db: Session):
        try:
            stmt = db.query(Menu).filter(self.model.id == id).first()
        except Exception as e:
            print(e)
            return False
        return stmt

    def updating_menu(self, id: uuid.UUID, data: schemas.Menu | schemas.Submenu, db: Session):
        updated_item = db.query(self.model).filter(self.model.id == id).first()
        updated_item.title = data.title
        updated_item.description = data.description
        db.add(updated_item)
        db.commit()
        db.refresh(updated_item)
        return updated_item

    def delete_menu(self, id: uuid.UUID, db: Session):
        deleted_item = db.query(self.model).filter(self.model.id == id).first()
        db.delete(deleted_item)
        db.commit()

    def get_rel_submenu(self, menu_id: uuid.UUID, db: Session):
        return db.query(Submenu).filter(Submenu.menu_id == menu_id).all()

    def creation_rel_submenu(self, menu_id: uuid.UUID, data: schemas.Menu | schemas.Submenu, db: Session):
        menu = db.query(Menu).filter(Menu.id == menu_id).first()
        created_item = Submenu(title=data.title, description=data.description, menu=menu)
        db.add(created_item)
        db.commit()
        db.refresh(created_item)
        return created_item

    def get_rel_submenu_by_id(self, menu_id: uuid.UUID, id: uuid.UUID, db: Session):
        return db.query(Submenu).filter(Submenu.id == id, Submenu.menu_id == menu_id).first()

    def updating_rel_submenu(self, menu_id: uuid.UUID, id: uuid.UUID, data: schemas.Submenu, db: Session):
        menu = db.query(Menu).filter(Menu.id == menu_id).first()
        updated_submenu = db.query(Submenu).filter(Submenu.id == id, Submenu.menu_id == menu_id).first()
        updated_submenu.title = data.title
        updated_submenu.description = data.description
        updated_submenu.menu = menu
        db.add(updated_submenu)
        db.commit()
        db.refresh(updated_submenu)
        return updated_submenu
