# Author: Katleho Gxagxa
# This is the bus service program of my application.
import random
from datetime import datetime, timedelta

# Constants
SEATS = 68
STANDS = 25
CAPACITY = SEATS + STANDS
FARE = 25  # Cost of a seat
STAND_FARE = FARE - 5  # Cost of a stand, 5 units less than a seat.

# Global variables
bus_id = ["1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108"]
left = bus_id.copy()  # Initialize with all buses available
balance = 0

# Tracks occupancy for each bus with random initial values
occupancy = {
    bus: {
        "seats": random.randint(0, SEATS),  # Random number of occupied seats
        "stands": random.randint(0, STANDS),  # Random number of occupied standing spots
    }
    for bus in bus_id
}


# Outputs the full bus schedule.
def bus_schedule():
    start_time = datetime.strptime("06:00", "%H:%M")
    end_time = datetime.strptime("22:00", "%H:%M")
    interval = timedelta(minutes=45)

    current_time = start_time
    times = []

    while current_time < end_time:
        times.append(current_time.strftime("%H:%M"))
        current_time += interval

    print("\nBus Schedule:")
    for time in times:
        print(f"Next trip to Auckland Park is at: {time}")


# Allows user to make a deposit.
def deposit():
    global balance
    amount = float(input("\nEnter amount to deposit: R"))
    balance += amount
    print(f"Your new balance is: R{balance:.2f}")


def order_ride():
    global balance, left, bus_id

    # Ensure there is enough balance to continue
    while balance < STAND_FARE:
        print("\nYour available amount is insufficient for a ride.")
        deposit()

    # Now proceed with ordering the ride
    for bus in left:
        # Calculate available seats and stands based on current occupancy
        seats_available = SEATS - occupancy[bus]["seats"]
        stands_available = STANDS - occupancy[bus]["stands"]

        if seats_available > 0:
            print(f"\n{seats_available} seats available in bus ID {bus}.")
            order = input("Order seat (Y/N)? ").casefold()
            if order in ("y", "yes"):
                print(
                    f"Seat ordered successfully in bus of ID - {bus}. Have a nice ride."
                )
                occupancy[bus]["seats"] += 1
                balance -= FARE
                print(f"Your new balance is: R{balance:.2f}")
                break
            elif order in ("n", "no"):
                print("Check bus schedule for the next available trip.")
            else:
                print("Invalid choice. Please enter Y/N.")

        elif stands_available > 0:
            print(f"\n{stands_available} standing spots available in bus ID {bus}.")
            order = input("Order stand (Y/N)? ").casefold()
            if order in ("y", "yes"):
                print(
                    f"Stand ordered successfully in bus of ID - {bus}. Have a nice ride."
                )
                occupancy[bus]["stands"] += 1
                balance -= STAND_FARE
                print(f"Your new balance is: R{balance:.2f}")
                break
            elif order in ("n", "no"):
                print("Check bus schedule for the next available trip.")
            else:
                print("Invalid choice. Please enter Y/N.")

        else:
            print(
                f"\nBus ID {bus} is full. Please check the bus schedule for the next available trip."
            )


def main(): ...


if __name__ == "__main__":
    main()
