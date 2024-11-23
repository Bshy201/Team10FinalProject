from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class CustomerBase(BaseModel):
    name: str
    email : str
    phone: str
    address: str


class CustomerCreate(CustomerBase):
    name : Optional[str]
    email : Optional[str]
    phone : Optional[str]
    address : Optional[str]


class CustomerUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]


class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True