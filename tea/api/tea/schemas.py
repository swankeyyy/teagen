from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class ProductBase(BaseModel):
    """Base model for all products(teas)"""
    name: str
    description: str
    cook_time: float
    price: str


class ProductCreate(ProductBase):
    pass


class Type(BaseModel):
    id: int
    name: str


class TeaCountry(BaseModel):
    id: int
    name: str


class Product(ProductBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    image: Optional[str] = None
    id: int
    tea_type: Type
    tea_country: TeaCountry


class TypeProduct(BaseModel):
    id: int
    name: str


class CountryProduct(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int
    name: str


class TypeList(Type):
    teas: list[TypeProduct]


class TeaCountryList(TeaCountry):
    teas: Optional[list[CountryProduct]] = None
