# Author: Katleho Gxagxa
# This is the main program of my application.
from registration import Registration
from login import LOGIN
import csv

def menu():
    menu = f'''
                      Welcome!
                 Create new account

                already have an Account?
                        LOG IN
    '''
    return menu


def option():
    while True:
        print("Choose option.")
        option = input("SIGN UP or LOG IN: ").strip().casefold()
        if option == "log in":
            user = LOGIN.get()
            user.match()
            break
        elif option == "sign up":
            user = Registration.get()
            user.check_user()
            user.store()
            print(user)
            break

def main():
    try:
        print(menu())
        option()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()