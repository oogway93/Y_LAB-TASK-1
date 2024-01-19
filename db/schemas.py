from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class MenuAddDTO(BaseModel):
    title: str
    description: str


class MenuDTO(MenuAddDTO):
    id: UUID
