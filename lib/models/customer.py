from .vehicle import Base
from sqlalchemy import Column, Integer, String, Date, Enum, Numeric, ForeignKey
from sqlalchemy.orm import relationship



class Customer(Base):
    __tablename__ = 'customers'

    customerid = Column(Integer, primary_key=True)
    FirstName = Column(String)
    LastName = Column(String)

    purchases = relationship("Purchase", back_populates="customer")
