import asyncio

import uvicorn
from fastapi import FastAPI

from handlers.handlers import router
from db.queries import RestaurantService
from db.models import metadata_obj

app = FastAPI(title="Task 1")
app.include_router(router)


async def main():
    RestaurantService.create_tables()


if __name__ == '__main__':
    asyncio.run(main())
    uvicorn.run("core:app", reload=True)
