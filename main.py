# Author: Katleho Gxagxa
# This is the main program of my application.
from registration import Registration
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
            print("logging in....  status: online.")
            break
        elif option == "sign up":
            user = Registration.get()
            user.store()
            print(user)
            break

def main():
    print(menu())
    option()


if __name__ == "__main__":
    main()