# Author: Katleho Gxagxa
# This is the main program of my application.
from registration import Registration
from service import bus_schedule, deposit, order_ride
from userlogin import LOGIN
import csv

def menu():
    menu_text = '''
    ================================
               Welcome!
    ================================
    1. Create New Account
    2. Log In to Existing Account
    3. Exit
    ================================
    '''
    return menu_text

def main_menu():
    while True:
        print(menu())
        choice = input("Please choose an option (1-3): ").strip()
        
        if choice == "1":
            user = Registration.get()
            user.check_user()
            user.store()
            print(user)
            break
        elif choice == "2":
            user = LOGIN.get()
            print("\n")
            user.match()
            service_menu()
            break
        elif choice == "3":
            print("Thank you for using the service. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")

            

def service_menu():
    while True:
        print("\n--- Bus Service Menu ---")
        print("1. View Bus Schedule")
        print("2. Deposit Money")
        print("3. Order a Ride")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            bus_schedule()
        elif choice == "2":
            deposit()
        elif choice == "3":
            order_ride()
        elif choice == "4":
            print("Thank you for using the bus service. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def main():
    try:
        main_menu()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()