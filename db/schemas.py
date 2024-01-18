from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str
    submenus_count: int | None = 0


class MenuOUT(MenuBase):
    id: int


