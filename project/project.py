# Author: Katleho Gxagxa
# This is the main program of my application.
from registration import Registration
from service import bus_schedule, deposit, order_ride
from userlogin import LOGIN
import csv


# The menu function here is displayed when the project first runs, allowing a user choice.
def menu():
    menu_text = """
    ================================
               Welcome!
    ================================
    1. Create New Account
    2. Log In to Existing Account
    3. Exit
    ================================
    """
    return menu_text


# This is the main menu of my application.
def main_menu():
    while True:
        print(menu())  # Calls and prints the main function.
        choice = input("Please choose an option (1-3): ").strip()

        # Action taken based on the user's choice.
        if choice == "1":  # The user is prompted to register.
            user = Registration.get()
            user.check_user()
            user.store()
            print(user)
            break
        elif choice == "2":
            user = LOGIN.get()  # The user is prompted to log in.
            print("\n")
            user.match()
            service_menu()  # service menu is called.
            break
        elif choice == "3":
            print("Thank you for using the service. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-3).")


# This function, service menu, allows the user to perform the ultimate functions of the application.
def service_menu():
    while True:  # Prompts the user for a valid choice.
        print("\n--- Bus Service Menu ---")
        print("1. View Bus Schedule")
        print("2. Deposit Money")
        print("3. Order a Ride")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            bus_schedule()  # if '1' is chosen, the bus_schedule() is called.
        elif choice == "2":
            deposit()  # if '2' is chosen, the deposit() is called.
        elif choice == "3":
            order_ride()  # if '3' is chosen, the order_ride() is called.
        elif choice == "4":
            print(
                "Thank you for using the bus service. Goodbye!"
            )  # if '4' is chosen, the whole application is exited.
            break
        else:
            print("Invalid choice. Please select a valid option.")


# main function of the application.
def main():
    try:
        main_menu()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
