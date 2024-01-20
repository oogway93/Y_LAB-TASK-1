import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder

from db import schemas
from db.database import get_db
from db.models import Submenu
from db.queries import CRUDRestaurantService

router = APIRouter(prefix="/api/v1/menus")

restaurant_service = CRUDRestaurantService(Submenu)


@router.post("/{menu_id}/submenus")
async def create_submenu(menu_id: uuid.UUID, data: schemas.Submenu = None, db: Session = Depends(get_db)):
    submenu_creation = restaurant_service.creation_rel_submenu(menu_id, data, db)
    if not submenu_creation:
        return Response(content="Error: Creation menu is failed", status_code=400)
    json_compatible_item_data = jsonable_encoder(submenu_creation)
    return JSONResponse(content=json_compatible_item_data, status_code=201)


@router.get("/{menu_id}/submenus/{id}")
async def get_submenu_by_menu_id(menu_id: uuid.UUID, id: uuid.UUID, db: Session = Depends(get_db)):
    submenu = restaurant_service.get_rel_submenu_by_id(menu_id, id, db)
    if not submenu:
        return JSONResponse(content={"detail": "submenu not found"}, status_code=404)
    return submenu


@router.get("/{menu_id}/submenus")
async def get_list_submenus(menu_id: uuid.UUID, db: Session = Depends(get_db)):
    return restaurant_service.get_rel_all_submenus(menu_id, db)


@router.patch("/{menu_id}/submenus/{id}")
async def update_submenu(menu_id: uuid.UUID, id: uuid.UUID, data: schemas.Submenu = None, db: Session = Depends(get_db)):
    updated_submenu = restaurant_service.updating_rel_submenu(menu_id, id, data, db)
    json_compatible_item_data = jsonable_encoder(updated_submenu)
    return JSONResponse(content=json_compatible_item_data)


@router.delete("/{menu_id}/submenus/{id}")
async def delete_submenu(menu_id: uuid.UUID, id: uuid.UUID, db: Session = Depends(get_db)):
    return restaurant_service.delete_submenu(menu_id, id, db)


