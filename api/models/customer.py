from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "costumer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(300))
    email = Column(String(300))
    phone = Column(String(300))
    address = Column(String(300))


    order = relationship("Orders", back_populates="customer")


