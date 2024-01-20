import uuid

from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from db.database import get_db
from db.queries import RestaurantService
from db import schemas

router = APIRouter(prefix="/api/v1")


@router.post("/menus", status_code=status.HTTP_201_CREATED)
async def create_menu(data: schemas.Menu = None, db: Session = Depends(get_db)):
    menu_creation = RestaurantService.creation_menu(data=data, db=db)
    if not menu_creation:
        return Response(content="Failed to create menu", status_code=400)
    json_compatible_item_data = jsonable_encoder(menu_creation)
    return JSONResponse(content=json_compatible_item_data, status_code=201)


@router.get("/menus/{id}")
async def get_menu_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    specified_menu = RestaurantService.getting_menu_by_id(id, db)
    if not specified_menu:
        return JSONResponse(content={"detail": "menu not found"}, status_code=404)
    return specified_menu


@router.get("/menus")
async def get_list_menus(db: Session = Depends(get_db)):
    return RestaurantService.getting_list_menus(db)


@router.patch("/menus/{id}")
async def update_menu(id: uuid.UUID, data: schemas.Menu = None, db: Session = Depends(get_db)):
    updated_menu = RestaurantService.updating_menu(id, data, db)
    json_compatible_item_data = jsonable_encoder(updated_menu)
    return JSONResponse(content=json_compatible_item_data)


@router.delete("/menus/{id}")
async def delete_menu(id: str, db: Session = Depends(get_db)):
    return RestaurantService.delete_menu(id, db)
