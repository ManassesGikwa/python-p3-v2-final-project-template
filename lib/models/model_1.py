from .vehicle import Base
from sqlalchemy import create_engine
# from .customer import Customer
from .purchase import Purchase
from .vehicle import Vehicle




if __name__ == '__main__':

    engine = create_engine('sqlite:///splendrous_motors.db') # SQLite database
    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine, tables=[Vehicle.__table__, Purchase.__table__])