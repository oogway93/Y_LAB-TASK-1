import uuid

from fastapi import APIRouter
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.responses import Response
from sqlalchemy.orm import Session

from db import schemas
from db.database import get_db
from db.models import Dish
from db.queries import CRUDRestaurantService

router = APIRouter(prefix="/api/v1/menus")

restaurant_service = CRUDRestaurantService(Dish)


@router.post("/{menu_id}/submenus/{submenu_id}/dishes")
async def create_dish(submenu_id: uuid.UUID, data: schemas.Dish, db: Session = Depends(get_db)):
    dish_creation = restaurant_service.create(data, db, submenu_id=submenu_id)
    if not dish_creation:
        return Response(content="Failed to create dish", status_code=400)
    json_compatible_item_data = jsonable_encoder(dish_creation)
    json_compatible_item_data["price"] = str(json_compatible_item_data["price"])
    return JSONResponse(content=json_compatible_item_data, status_code=201)


@router.get("/{menu_id}/submenus/{submenu_id}/dishes/{id}")
async def get_dish(id: uuid.UUID, db: Session = Depends(get_db)):
    dish = restaurant_service.read(db, id)
    if dish is not None:
        dish.price = str(dish.price)
    if not dish:
        return JSONResponse(content={"detail": "dish not found"}, status_code=404)
    return dish


@router.get("/{menu_id}/submenus/{submenu_id}/dishes")
async def get_all_dishes(db: Session = Depends(get_db)):
    return restaurant_service.read_all(db)


@router.patch("/{menu_id}/submenus/{submenu_id}/dishes/{id}")
async def update_dish(id: uuid.UUID, data: schemas.Dish, db: Session = Depends(get_db)):
    updated_dish = restaurant_service.update(data, db, id)
    json_compatible_item_data = jsonable_encoder(updated_dish)
    json_compatible_item_data["price"] = str(jsonable_encoder(updated_dish)["price"])
    return JSONResponse(content=json_compatible_item_data)


@router.delete("/{menu_id}/submenus/{submenu_id}/dishes/{id}")
async def delete_dish(id: uuid.UUID, db: Session = Depends(get_db)):
    restaurant_service.delete(db, id)
