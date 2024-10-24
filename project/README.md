# Order Bus Service.
    #### Video Demo:  <URL HERE>
    #### Description:

Every line of code is written by Katleho Gxagxa.
Some lines on the test_project.py were achieved with the help of Stack Overflow, cs50.ai and chatGPT. Prompting for guidance. The concept of Mock testing was new to me.

For style, I used black:
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)                           


My application aims to provide an automated way in which to order a ride on a bus. This can of course be adapted for any form of service in which the ordering process is similar, like ordering a ride on a car, or a meal at a restaurant or any other such similar occurences. 

The first feature I will discuss is the registration feature. I wrote this feature to make sure that the user's of the application can receive control of their privacy. This allowed me to use a csv file to store user information. This feature has a check user method that is designed to check if the user has already registered, this prioritises email addresses primarily. The logic behind this is that a user is allowed to use an email address only once. Making sure that the user can create another account using a different email address for other purposes, i.e. business. The function raises exceptions if a user inputs a name, middle name (which is optional btw), or last name that is not exclusively composed of only alphabets. The validators library is used to check the validity of the user's email address. I use regular expressions to assess the format of a user's choice of password, this allows me to constrain the password to the desired format.

The second feature I will discuss is the log in feature. This feature is designed to accept two inputs from the user, their email address and their password. The input is then checked against stored data, if the user is in the database, the user is allowed to use the rest of the features.
In the case that the user has no valid credentials, the program exits, informing the user that the account does not exist.

The final feature that I will discuss besides the project.py and test_project.py is the service feature. This feature is the essence of my application. This feature uses the datetime library to output a bus schedule via the bus_schedule() module. It allows the user to deposit funds for a trip, where a seat costs R25 and a stand costs only R20. If the user's balance is less than the cost of transit, the user cannot order a ride, otherwise the user is allowed to order a ride, under some conditions. If all the seats are occupied, the user is prompted to order a stand. Seats are prioritised over standing, for practical reasons. The user can choose not to order a ride in the current bus and choose from a range of 8 available buses. The time of departure will be influenced by the user's discretion and the time shown at the menu once the user logs in.

The project is then run in my projects file, where the logic of the whole app is. The menu function is first called, prompting the user to choose what they wish to do, 1. Create a new account, 2. Log in to existing account, or 3. Exit. This menu then reacts accordingly to user input. Where the function discussed above get called. 

The test_project contains tests for every function in the project.py file. This one is interesting, having never learned how to test functions with such functionality before (functions receiving input and querying csv files). I had to approach the fact that I still have so much learning to do by myself. As it was encouraged in almost every other lecture I watched. The links that were often displayed on screen became a useful route to learning about a lot of the functionality I then used in my programs. In this one especially, I had to learn what mock testing is and how it work. I have in many instances convinced myself to resort to the @pytest.mark.skip(reason="no way of currently testing this") method to avoid any further confusion learning to mock test. I used Stack Overflow, cs50.ai and chatGPT for guidance in write some parts of this code. The following links came in handy for learning the basics:  
    https://docs.python.org/3/library/unittest.mock.html
    https://docs.pytest.org/en/stable/getting-started.html

I had to create mock csv data to mimic a user and their subsequent inputs. This is the most learning I had to do while writing this application. The result of which is a greater desire to learn more of what python can do.


There are some feature flaws here that I would like to confront. The application does not at all save the user's balance to retrieve it whenever they log in again. This would be ideal. The reason I was not able to implement the feature here is that I would have to learn about linking the User's csv file to that of balances. Which is a great idea to think about. This would have made my program a lot more complicated. I enrolled for CS50 SQL to learn about databases and how they interact with each other. I hope to return to this program and improve on it in future.