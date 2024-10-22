# AUTHOR: Katleho Gxagxa
# This program implements the log in functionality to my application.
from registration import Registration
import csv
from datetime import datetime

class LOGIN():
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    @classmethod
    def get(cls):
        email = input("Email: ")
        password = input("Password: ")
        return cls(email, password)

    def match(self):
        with open("Users.csv", "r") as user_database:
            reader = csv.DictReader(user_database)
            for row in reader:
                if row["email"] == self.email and row["password"] == self.password:
                    print(f'''  Logging in...
                    Status: Online.''')
                    profile = f'''
                    First name: {row["first_name"]}
                    Middle name: {row["middle_name"]}
                    Last name: {row["last_name"]}
                    Email: {row["email"]}
                    Date of Birth: {row["birth_date"]}
                    Gender: {row["gender"]}

                                            {datetime.now()}
                    '''
                    print(profile)
                    break
            else:
                raise ValueError("Account does not exist.")
    

def main():
    ...

if __name__ == "__main__":
    main()