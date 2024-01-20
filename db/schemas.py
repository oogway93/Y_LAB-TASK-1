from uuid import UUID
from typing import Optional

from pydantic import BaseModel


class Menu(BaseModel):
    title: str
    description: str

#     class Config:
#         from_attributes = True
#
#
# class MenuDTO(MenuAddDTO):
#     id: int
#
#     class Config:
#         from_attributes = True
