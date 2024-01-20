from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class Menu(BaseModel):
    title: str
    description: str


class Submenu(BaseModel):
    title: str
    description: str
