# AUTHOR: Katleho Gxagxa
# This program implements the log in functionality to my application.
from registration import Registration
import csv

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
                    break
                else:
                    pass
            else:
                raise ValueError("Account does not exist.")
    

def main():
    ...

if __name__ == "__main__":
    main()