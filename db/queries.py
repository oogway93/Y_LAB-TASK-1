import uuid

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from db.database import async_engine, Base, engine, SessionLocal
from db.models import Menu, Submenu, Dish
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

    def get_all_menus(self, db: Session):
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

    def get_rel_all_submenus(self, menu_id: uuid.UUID, db: Session):
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

    def delete_submenu(self, menu_id: uuid.UUID, id: uuid.UUID, db: Session):
        deleted_submenu = db.query(Submenu).filter(Submenu.id == id, Submenu.menu_id == menu_id).first()
        db.delete(deleted_submenu)
        db.commit()

    def get_rel_all_dishes(self, submenu_id: uuid.UUID, db: Session):
        return db.query(self.model).all()

    def create_rel_dish(self, submenu_id: uuid.UUID, data: schemas.Dish, db: Session):
        table = self.model(**data.dict())
        print(table.price, type(table.price))
        table.price = str(data.price)
        print(table.price, type(table.price))
        print(table)
        table.submenu_id = submenu_id
        try:
            db.add(table)
            db.commit()
            db.refresh(table)
        except Exception as e:
            print(e)
            return False
        return table

    def get_rel_dish_by_id(self, submenu_id: uuid.UUID, id: uuid.UUID, db: Session):
        return db.query(Dish).filter(Dish.id == id).first()

    def delete_dish(self, id: uuid.UUID, db: Session):
        deleted_submenu = db.query(Dish).filter(Dish.id == id).first()
        db.delete(deleted_submenu)
        db.commit()

    def update_dish(self, id: uuid.UUID, data: schemas.Dish, db: Session):
        table = db.query(self.model).filter(self.model.id == id).first()
        table.title = data.title
        table.description = data.description
        table.price = data.price
        db.add(table)
        db.commit()
        db.refresh(table)
        return table
  