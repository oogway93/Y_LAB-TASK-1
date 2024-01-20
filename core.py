import asyncio

import uvicorn
from fastapi import FastAPI

from handlers.handlers_menu import router
from handlers.handlers_submenu import router as router2
from db.queries import CRUDRestaurantService
from db.models import metadata_obj

app = FastAPI(title="Task 1")
app.include_router(router)
app.include_router(router2)


async def main():
    CRUDRestaurantService.create_tables()


if __name__ == '__main__':
    asyncio.run(main())
    uvicorn.run("core:app", reload=True)
