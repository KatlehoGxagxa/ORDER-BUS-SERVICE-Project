# Author: Katleho Gxagxa.
# This program seeks to create a registration function for a user of an application.
import validators
import re

class Registration():
    def __init__(self, first_name, last_name, email, birth_date, gender, password, middle_name=None):
        self.first_name = first_name
        self.middle_name = middle_name 
        self.last_name = last_name
        self.email = email
        self.birth_date = birth_date
        self.gender = gender
        self.password = password
    
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
        if middle_name == None:
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
          

    def __str__(self):
        result = f'''
    First Name: {self.first_name}
    Middle Name: {self.middle_name}
    Last Name: {self.last_name}
    Email: {self.email}
    Date of Birth: {self.birth_date}
    Gender: {self.gender}
    '''
        return result
    
    @classmethod
    def get(cls):
        first_name = input("First name: ").strip().capitalize()
        middle_name = input("Middle name (Optional): ").strip().capitalize()
        last_name = input("Last name: ").strip().capitalize()
        email = input("Email: ").strip()
        birth_date = input("Date of Birth (YYYY-MM-DD): ").strip()
        gender = input("Gender (M or F or Other): ").strip().casefold()
        return cls(first_name, last_name, email, birth_date, gender, middle_name)

def main():
    while True:
        try:
            user = Registration.get()
            print(user)
            break
        except ValueError as e:
            print(f"Error: {e}")
            pass
    
# TODO
# Have password work either by conditionals or regex.


if __name__ == "__main__":
    main()