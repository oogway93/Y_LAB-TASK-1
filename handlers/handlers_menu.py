import uuid

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session

from db import schemas
from db.database import get_db
from db.models import Menu
from db.queries import CRUDRestaurantService

router = APIRouter(prefix="/api/v1")

restaurant_service = CRUDRestaurantService(Menu)


@router.post("/menus")
async def create_menu(data: schemas.Menu = None, db: Session = Depends(get_db)):
    menu_creation = restaurant_service.creation_menu(data, db)
    if not menu_creation:
        return Response(content="Error: Creation menu is failed", status_code=400)
    json_compatible_item_data = jsonable_encoder(menu_creation)
    return JSONResponse(content=json_compatible_item_data, status_code=201)


@router.get("/menus/{id}")
async def get_menu_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    menu = restaurant_service.getting_menu_by_id(id, db)
    if not menu:
        return JSONResponse(content={"detail": "menu not found"}, status_code=404)
    return menu


@router.get("/menus")
async def get_all_menus(db: Session = Depends(get_db)):
    return restaurant_service.get_all_menus(db)


@router.patch("/menus/{id}")
async def update_menu(id: uuid.UUID, data: schemas.Menu = None, db: Session = Depends(get_db)):
    updated_menu = restaurant_service.updating_menu(id, data, db)
    json_compatible_item_data = jsonable_encoder(updated_menu)
    return JSONResponse(content=json_compatible_item_data)


@router.delete("/menus/{id}")
async def delete_menu(id: uuid.UUID, db: Session = Depends(get_db)):
    return restaurant_service.delete_menu(id, db)
