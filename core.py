import asyncio

import uvicorn
from fastapi import FastAPI


app = FastAPI(title="Task 1")


async def main():
    pass


if __name__ == '__main__':
    asyncio.run(main())
    uvicorn.run("core:app", reload=True)
