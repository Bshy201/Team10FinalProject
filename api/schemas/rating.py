from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class RatingBase(BaseModel):
    description: str


class RatingCreate(RatingBase):
    description: str

class RatingUpdate(BaseModel):
    description: str


class Rating(RatingBase):
    id: int
    order_id: int
    description: str

    class ConfigDict:
        from_attributes = True