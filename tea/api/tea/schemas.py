from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProductBase(BaseModel):
    """Base model for all products(teas)"""

    name: str
    description: str
    cook_time: float
    price: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    image: str
    id: int
