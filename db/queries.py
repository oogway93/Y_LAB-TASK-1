import logging
import uuid
from typing import Optional

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import IntegrityError

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

    def create(
            self,
            data: schemas.Menu | schemas.Submenu | schemas.Dish,
            db: Session,
            menu_id: uuid.UUID = None,
            submenu_id: uuid.UUID = None,
            id: uuid.UUID = None
    ):
        table = self.model(**data.dict())
        if id is not None:
            table.id = id
        if menu_id is not None:
            table.menu_id = menu_id
        if submenu_id is not None:
            table.submenu_id = submenu_id
        try:
            db.add(table)
            db.commit()
            db.refresh(table)
        except IntegrityError as e:
            logging.info(e)
            return False
        return table

    def read(
            self,
            db: Session,
            id: uuid.UUID = None,
    ):
        if id:
            result = db.query(self.model).filter(self.model.id == id).first()
            if self.model == Menu and result is not None:
                submenu_count = db.query(Submenu).filter(Submenu.id == id).count()
                dish_count = (db.query(Dish)
                              .join(Submenu, Dish.submenu_id == Submenu.id)
                              .filter(Submenu.menu_id == id)
                              .count())
                result.submenu_count = submenu_count
                result.dish_count = dish_count
            if self.model == Submenu and result is not None:
                dish_count = (
                    db.query(Dish)
                    .filter(Dish.submenu_id == id)
                    .count()
                )
                result.dish_count = dish_count
            return result

    def read_all(
            self,
            db: Session
    ):
        return db.query(self.model).all()

    def update(
            self,
            data: schemas.Menu | schemas.Submenu | schemas.Dish,
            db: Session,
            id: uuid.UUID = None
    ):
        table = db.query(self.model).filter(self.model.id == id).first()
        for key, value in data.dict().items():
            setattr(table, key, value)
        try:
            db.add(table)
            db.commit()
            db.refresh(table)
        except IntegrityError as e:
            logging.info(e)
        return table

    def delete(
            self,
            db: Session,
            id: uuid.UUID = None
    ):
        table = db.query(self.model).filter(self.model.id == id).first()
        db.delete(table)
        db.commit()
        return table
