from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from faker import Faker
from lib.models.vehicle import Base, Vehicle
from lib.models.customer import Customer
from lib.models.purchase import Purchase

# Create SQLAlchemy engine
engine = create_engine('sqlite:///splendrous_motors.db')

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)

# Use context manager for session
with DBSession() as session:
    # Add fake customer data
    fake = Faker()
    try:
        # Check if the customers table exists
        inspector = inspect(engine)
        if not inspector.has_table('customers'):
            print("Error: The customers table doesn't exist.")
        else:
            for _ in range(50):
                customer = Customer(
                    FirstName=fake.first_name(),
                    LastName=fake.last_name()
                )
                session.add(customer)

            # Generate and insert fake vehicle data with default registration status "No" and no license plates
            for _ in range(50):
                vehicle = Vehicle(
                    make=fake.company(),
                    color=fake.color_name(),
                    registration_status='No',
                    car_Regno=None,  # No default license plate
                    price=fake.random_number(digits=5)
                )
                session.add(vehicle)

            # Generate and insert fake purchase data
            for _ in range(50):
                amount_paid = fake.random_number(digits=5)
                purchase = Purchase(
                    amount_paid=amount_paid,
                    purchase_type='Hire-purchase',
                    payment_status=f'Cleared ({amount_paid})'  # Assuming initial payment clears the balance
                )
                session.add(purchase)

            # Commit the changes
            session.commit()

            print("Data added successfully!")
    except SQLAlchemyError as e:
        print(f"An error occurred: {str(e)}")
        session.rollback()
