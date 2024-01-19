from uuid import UUID

from fastapi import APIRouter, Response, Form, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from db.queries import AsyncORM
from db import schemas
from db.schemas import MenuDTO

router = APIRouter(prefix="/api/v1")


@router.post("/menus", status_code=status.HTTP_201_CREATED)
async def create_menu(menu: schemas.MenuAddDTO):
    await AsyncORM.creation_menu(menu.title, menu.description)
    return menu


@router.get("/menus")
async def get_list_menu():
    menus = await AsyncORM.getting_list_menu()
    if menus is None:
        return []
    return menus


@router.get("/menus/{id}")
async def get_menu_by_id(id: UUID, data: MenuDTO, db: Session = Depends(get_db)):
    menu = await AsyncORM.getting_menu_by_id(id, db)
    if not menu:
        return JSONResponse(content={"detail": "menu not found"}, status_code=404)
    return data


@router.patch("/menus/{id}")
async def update_menu(id: UUID, menu: schemas.MenuAddDTO):
    return await AsyncORM.updating_menu(id, menu.title, menu.description)


@router.delete("/menus/{id}")
async def delete_menu(id: UUID):
    return await AsyncORM.delete_menu(id)