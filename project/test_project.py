# Author: Katleho Gxagxa
# This program writes tests for the project.py file of our application.
from registration import Registration
from service import bus_schedule, deposit, order_ride
from userlogin import LOGIN
import csv
import pytest
from project import menu, main_menu, service_menu
from unittest.mock import patch, MagicMock, mock_open


def test_menu():
    expected_output = """
    ================================
               Welcome!
    ================================
    1. Create New Account
    2. Log In to Existing Account
    3. Exit
    ================================
    """
    assert menu() == expected_output


def test_main_menu_bus_schedule():
    # Mock data for Users.csv with a matching user
    mock_csv_data = """email,password,first_name,middle_name,last_name,birth_date,gender
test@example.com,123456,John,Doe,Smith,1990-01-01,Male"""

    # Mock the file open function to use the mock data
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        # Mock input sequence to navigate through initial menu
        input_sequence = iter(
            ["2", "test@example.com", "123456", "1", "4"]
        )  # Log in, choose Bus Schedule, then Exit

        with patch("builtins.input", lambda _: next(input_sequence)):
            with patch("project.bus_schedule") as mock_bus_schedule:
                main_menu()  # Call main_menu function
                mock_bus_schedule.assert_called_once()


def test_main_menu_deposit():
    # Mock data for Users.csv with a matching user
    mock_csv_data = """email,password,first_name,middle_name,last_name,birth_date,gender
test@example.com,123456,John,Doe,Smith,1990-01-01,Male"""

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        input_sequence = iter(
            ["2", "test@example.com", "123456", "2", "4"]
        )  # Log in, select Deposit Funds, then Exit

        with patch("builtins.input", lambda _: next(input_sequence)):
            with patch("project.deposit") as mock_deposit:
                main_menu()  # Call main_menu function
                mock_deposit.assert_called_once()


def test_main_menu_order_ride():
    # Mock data for Users.csv with a matching user
    mock_csv_data = """email,password,first_name,middle_name,last_name,birth_date,gender
test@example.com,123456,John,Doe,Smith,1990-01-01,Male"""

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        input_sequence = iter(
            ["2", "test@example.com", "123456", "3", "4"]
        )  # Log in, choose Order a Ride, then Exit

        with patch("builtins.input", lambda _: next(input_sequence)):
            with patch("project.order_ride") as mock_order_ride:
                main_menu()  # Call main_menu function
                mock_order_ride.assert_called_once()


def test_main_menu_logout(capfd):
    input_sequence = iter(["3"])  # Simulating the input for option "3"

    with patch("builtins.input", lambda _: next(input_sequence)):
        main_menu()  # Call the main_menu function

    # Capture the output
    captured = capfd.readouterr()

    expected_output = "Thank you for using the service. Goodbye!"
    assert (
        expected_output in captured.out
    )  # Check if the expected output is in the captured output


def test_service_menu_exit(capfd):
    input_sequence = iter(["4"])  # Simulate input for exiting the service menu

    with patch("builtins.input", lambda _: next(input_sequence)):
        service_menu()  # Call the service_menu function

    # Capture the output
    captured = capfd.readouterr()

    expected_output = "Thank you for using the bus service. Goodbye!"
    assert (
        expected_output in captured.out
    )  # Check if the expected output is in the captured output
