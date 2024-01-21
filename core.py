import asyncio

import uvicorn
from fastapi import FastAPI

from db.queries import CRUDRestaurantService
from handlers.handlers_dish import router as dish_router
from handlers.handlers_menu import menu_router
from handlers.handlers_submenu import router as submenu_router

app = FastAPI(title="Task 1")
app.include_router(menu_router)
app.include_router(submenu_router)
app.include_router(dish_router)


async def main():
    CRUDRestaurantService.create_tables()


if __name__ == '__main__':
    asyncio.run(main())
    uvicorn.run("core:app", reload=True, host="0.0.0.0")
