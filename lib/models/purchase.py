from .vehicle import Base
from sqlalchemy import Column, Integer, Numeric, Enum, Date, ForeignKey
from sqlalchemy.orm import relationship
from .customer import Customer
from .vehicle import Vehicle

class Purchase(Base):
    __tablename__ = 'purchases'

    purchaseId = Column(Integer, primary_key=True)
    amount_paid = Column(Numeric)
    purchase_type = Column(Enum('Cash', 'Hire-purchase'))
    Date = Column(Date)
    payment_status = Column(Enum('Cleared', 'Ongoing'))

    customer_id = Column(Integer, ForeignKey('customers.customerid'))
    customer = relationship(Customer, back_populates="purchases")

    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicleId'))
    vehicle = relationship(Vehicle, back_populates="purchases")
