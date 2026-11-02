from pydantic import BaseModel, ConfigDict
from typing import List


class ItemBase(BaseModel):
    name: str
    description: str = ""
    price: float = 0.0


class ItemCreate(ItemBase):
    pass


class ItemOut(ItemBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ImportCsvRequest(BaseModel):
    csv_path: str


class DeleteRequest(BaseModel):
    ids: List[int]