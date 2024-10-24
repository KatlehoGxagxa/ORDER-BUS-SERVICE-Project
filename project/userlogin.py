# AUTHOR: Katleho Gxagxa
# This program implements the log in functionality to my application.
from registration import Registration
import csv
from datetime import datetime


# This log in class contains only two attributes. Used to allow the user to use the application.
class LOGIN:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    # This class method gets these required attributes from the user.
    @classmethod
    def get(cls):
        email = input("Email: ")
        password = input("Password: ")
        return cls(email, password)

    # This match function checks if the user is in the User csv file or not.
    def match(self):
        with open("Users.csv", "r") as user_database:
            reader = csv.DictReader(user_database)
            for row in reader:
                if row["email"] == self.email and row["password"] == self.password:
                    print(
                        f"""  Logging in...
                    Status: Online."""
                    )
                    profile = f"""
                    First name: {row["first_name"]}
                    Middle name: {row["middle_name"]}
                    Last name: {row["last_name"]}
                    Email: {row["email"]}
                    Date of Birth: {row["birth_date"]}
                    Gender: {row["gender"]}

                                            {datetime.now()}
                    """
                    print(profile)
                    break
            else:
                raise ValueError("Account does not exist.")


def main(): ...


if __name__ == "__main__":
    main()
