from fastapi import APIRouter, Response, Form, status

from db.queries import AsyncORM
from db import schemas

router = APIRouter(prefix="/api/v1")


@router.post("/menus", status_code=status.HTTP_201_CREATED)
async def create_menu(menu: schemas.MenuBase):
    await AsyncORM.creation_menu(menu.title, menu.description, menu.submenus_count)
    return menu


@router.get("/menus")
async def get_list_menu():
    menus = await AsyncORM.getting_menu()
    return menus

