# Author: Katleho Gxagxa.
# This program seeks to create a registration function for a user of an application.
import validators
import re
import csv

class Registration():
    def __init__(self, first_name, last_name, email, birth_date, gender, password, middle_name=None):
        self.first_name = first_name 
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date
        self.gender = gender
        self.password = password
        self.middle_name = middle_name

    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not (len(first_name) >= 2 and first_name.isalpha()):
            raise ValueError("Invalid first name.")
        self._first_name = first_name
        
    
    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        if not middle_name:
            self._middle_name = ""
        else:
            if not (len(middle_name) >= 2 and middle_name.isalpha()):
                raise ValueError("Invalid middle name.")
            else:
                self._middle_name = middle_name
            

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if not (len(last_name) >= 2 and last_name.isalpha()):
            raise ValueError("Invalid middle name.")
        else:
            self._last_name = last_name.capitalize()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if not validators.email(email):
            raise ValueError("Invalid email")
        else:
            self._email = email

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, gender):
        match gender:
            case "m":
                self._gender = "Male"
            case "male":
                self._gender = "Male"
            case "f":
                self._gender = "Female"
            case "female":
                self._gender = "Female"
            case "other":
                self._gender = "Other"
            case "o":
                self._gender = "Other"
            case _:
                raise ValueError("Invalid gender")
            
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, birth_date):
        pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'
        if not re.match(pattern, birth_date):
            raise ValueError("Date of Birth format YYYY-MM-DD")
        else:
            self._birth_date = birth_date
          
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        error_message = f'''
        1. Contains at least one letter (uppercase or lowercase).
        2. Contains at least two digits.
        3. Contains at least one special character (e.g., !@#$%^&*()).
        4. Has a length of at least 8 characters.
        '''
        pattern = r'^(?=.*[a-zA-Z])(?=(?:.*\d.*\d))(?=.*[!@#$%^&*()])[A-Za-z\d!@#$%^&*()]{8,}$'
        if not re.match(pattern, password):
            raise ValueError(error_message)
        else:
            self._password = password


    def __str__(self):
        result = f'''
Successfully registered.
    '''
        return result
    
    @classmethod
    def get(cls):
        for_password = f'''
        1. Contains at least one letter (uppercase or lowercase).
        2. Contains at least two digits.
        3. Contains at least one special character (e.g., !@#$%^&*()).
        4. Has a length of at least 8 characters.
        '''
        first_name = input("First name: ").strip().capitalize()
        middle_name = input("Middle name (Optional): ").strip().capitalize()
        last_name = input("Last name: ").strip().capitalize()
        email = input("Email: ").strip()
        birth_date = input("Date of Birth (YYYY-MM-DD): ").strip()
        gender = input("Gender (M or F or Other): ").strip().casefold()
        password = input(f"Enter Password:  {for_password} ")
        return cls(first_name, last_name, email, birth_date, gender, password, middle_name)


    def store(self):
        with open("Users.csv", "w") as user_database:
            headers = ["first_name", "middle_name", "last_name", "email", "birth_date", "gender", "password"]
            writer = csv.DictWriter(user_database, fieldnames=headers)
            writer.writeheader()
            writer.writerow({'first_name': self.first_name, "middle_name": self.middle_name, "last_name": self.last_name, "email": self.email, "birth_date": self.birth_date, "gender": self.gender, "password": self.password})

def main():
    ...    

if __name__ == "__main__":
    main()