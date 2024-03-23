# Importing necessary modules
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Numeric
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()


# Define the Vehicle class
class Vehicle(Base):
    __tablename__ = 'vehicles'

    vehicleId = Column(Integer, primary_key=True)
    make = Column(String)
    color = Column(String)
    registration_status = Column(String)
    car_Regno = Column(String)
    price = Column(Numeric)

    purchases = relationship("Purchase", back_populates="vehicle")




