# Author: Katleho Gxagxa.
# This program seeks to create a registration function for a user of an application.
class Registration():
    def __init__(self, first_name, last_name, email, birth_date, gender, password, middle_name=None):
        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._email = email
        self._birth_date = birth_date
        self._gender = gender
        self._password = password

    def __str__(self):
        output = f'''   
                    First Name: {self._first_name}
                    Middle Name: {self._middle_name}
                    Last Name: {self._last_name}
                    Email: {self._email}
                    Date of Birth: {self._birth_date}
                    Gender: {self._gender}
                '''
        print(output)


user = Registration("Katleho", "Gxagxa", "gxagxakatleho@gmail.com", "1998/10/11", "M", "password")
print(user)


# TODO
# Validate email addresses. Make sure birth_date is handled using either conditionals or regex. have password work either conditionals or regex.
# All name variables should be just alphabets and real names.