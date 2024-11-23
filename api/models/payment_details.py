from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class PaymentDetails(Base):
    __tablename__ = "payment_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    payment_type = Column(String(300))
    payment_status = Column(String(300))


    order_detail = relationship("Order_Details", back_populates="payment_details")


