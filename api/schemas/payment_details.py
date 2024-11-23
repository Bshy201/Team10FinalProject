from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .sandwiches import Sandwich


class PaymentDetailBase(BaseModel):
    payment_type: str


class PaymentDetailCreate(PaymentDetailBase):
    order_details_id: int

class PaymentDetailUpdate(BaseModel):
    order_details_id: Optional[int] = None




class PaymentDetail(PaymentDetailBase):
    id: int
    order_id: int
    sandwich: Sandwich = None

    class ConfigDict:
        from_attributes = True