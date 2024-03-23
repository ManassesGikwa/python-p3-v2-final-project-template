# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from models.vehicle import Vehicle
# from models.purchase import Purchase

# engine = create_engine('sqlite:///splendrous_motors.db')

# Session = sessionmaker(bind=engine)
# session = Session()

# def make_purchase(session):
#     while True:
#         vehicle_ids = input("Enter the Vehicle IDs of the vehicles you want to buy (separated by commas): ").split(',')
#         selected_vehicles = session.query(Vehicle).filter(Vehicle.vehicleId.in_(vehicle_ids)).all()

#         total_price = sum(vehicle.price for vehicle in selected_vehicles)
#         print("Selected Vehicles:")
#         for vehicle in selected_vehicles:
#             print(f"Vehicle ID: {vehicle.vehicleId}, Make: {vehicle.make}, Color: {vehicle.color}, Price: {vehicle.price}")

#         print(f"Total Price: {total_price}")

#         payment_choice = input("Choose payment method (1 for cash/2 for hirepurchase): ")
#         if payment_choice == '1':
#             print("Proceed to the office for directions on cash transactions.")
#             break
#         elif payment_choice == '2':
#             balance = total_price
#             while balance > 0:
#                 try:
#                     payment = float(input("Enter payment amount: "))
#                     if payment <= 0:
#                         raise ValueError("Payment amount must be positive.")
#                     balance -= payment
#                     if balance < 0:
#                         print("You have overpaid. Please enter a valid payment.")
#                         balance += payment
#                     print(f"Your balance is now: {balance}")
#                 except ValueError as e:
#                     print("Invalid input. Please enter a valid positive number for payment.")
#             print("Congratulations! You have finished paying for your car. You are now a full car owner!")
#             break
#         else:
#             print("Invalid payment method. Please choose '1' for cash or '2' for hirepurchase.")

# def main(session):
#     print("Welcome to Splendrous Motors")
#     while True:
#         print("What would you like to do?")
#         print("1. See all available vehicles")
#         print("2. Enquire on a vehicle")
#         choice = input("Enter your choice (1/2): ")

#         if choice == '1':
#             # Display all available vehicles
#             vehicles = session.query(Vehicle).all()
#             print("Available Vehicles:")
#             for vehicle in vehicles:
#                 print(f"Vehicle ID: {vehicle.vehicleId}, Make: {vehicle.make}, Color: {vehicle.color}, Price: {vehicle.price}")

#         elif choice == '2':
#             search_query = input("Enter vehicle ID, make, or color: ")
#             vehicles = session.query(Vehicle).filter(
#                 Vehicle.vehicleId.like(f'%{search_query}%') |
#                 Vehicle.make.like(f'%{search_query}%') |
#                 Vehicle.color.like(f'%{search_query}%')
#             ).all()
#             if vehicles:
#                 print("Matching Vehicles:")
#                 for vehicle in vehicles:
#                     print(f"Vehicle ID: {vehicle.vehicleId}, Make: {vehicle.make}, Color: {vehicle.color}, Price: {vehicle.price}")
#                 purchase_choice = input("Would you like to make a purchase? (yes/no): ")
#                 if purchase_choice.lower() == 'yes':
#                     make_purchase(session)
#             else:
#                 print("No vehicles found matching the search query.")

#         else:
#             print("Invalid choice. Please enter 1 or 2.")

# if __name__ == "__main__":
#     main(session)


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.vehicle import Vehicle
from models.purchase import Purchase
from decimal import Decimal

engine = create_engine('sqlite:///splendrous_motors.db')

Session = sessionmaker(bind=engine)
session = Session()

def make_purchase():
    while True:
        vehicle_ids = input("Enter the Vehicle IDs of the vehicles you want to buy (separated by commas): ").split(',')
        selected_vehicles = session.query(Vehicle).filter(Vehicle.vehicleId.in_(vehicle_ids)).all()

        total_price = sum(vehicle.price for vehicle in selected_vehicles)
        print("Selected Vehicles:")
        for vehicle in selected_vehicles:
            print(f"Vehicle ID: {vehicle.vehicleId}, Make: {vehicle.make}, Color: {vehicle.color}, Price: {vehicle.price}")

        print(f"Total Price: {total_price}")

        payment_choice = input("Choose payment method (1 for cash/2 for hirepurchase): ")
        if payment_choice == '1':
            print("Proceed to the office for directions on cash transactions.")
            break
        elif payment_choice == '2':
            balance = Decimal(total_price)
            while balance > 0:
                try:
                    payment = Decimal(input("Enter payment amount: "))
                    if payment <= 0:
                        raise ValueError("Payment amount must be positive.")
                    balance -= payment
                    if balance < 0:
                        print("You have overpaid. Please enter a valid payment.")
                        balance += payment
                    print(f"Your balance is now: {balance}")
                except ValueError as e:
                    print("Invalid input. Please enter a valid positive number for payment.")
            print("Congratulations! You have finished paying for your car. You are now a full car owner!")
            break
        else:
            print("Invalid payment method. Please choose '1' for cash or '2' for hirepurchase.")

def main():
    print("Welcome to Splendrous Motors")
    while True:
        print("What would you like to do?")
        print("1. See all available vehicles")
        print("2. Enquire on a vehicle")
        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            # Display all available vehicles
            vehicles = session.query(Vehicle).all()
            print("Available Vehicles:")
            for vehicle in vehicles:
                print(f"Vehicle ID: {vehicle.vehicleId}, Make: {vehicle.make}, Color: {vehicle.color}, Price: {vehicle.price}")

        elif choice == '2':
            search_query = input("Enter vehicle ID, model, make, or color: ")
            # Query vehicles by search query
            vehicles = session.query(Vehicle).filter(
                Vehicle.vehicleId.like(f'%{search_query}%') |
                Vehicle.make.like(f'%{search_query}%') |
                Vehicle.color.like(f'%{search_query}%')
            ).all()
            if vehicles:
                print("Matching Vehicles:")
                for vehicle in vehicles:
                    print(f"Vehicle ID: {vehicle.vehicleId}, Make: {vehicle.make}, Color: {vehicle.color}, Price: {vehicle.price}")
                purchase_choice = input("Would you like to make a purchase? (yes/no): ")
                if purchase_choice.lower() == 'yes':
                    make_purchase()
            else:
                print("No vehicles found matching the search query.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
