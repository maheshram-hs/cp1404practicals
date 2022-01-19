"""
Taxi simulator program that uses my Taxi and SilverServiceTaxi classes.

Taxi Simulator. Created by Maheshram Shunmuganand, January 2022
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """make use of Taxi and SilverServiceTaxi classes."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print(f"Let's drive!\n{MENU}")
    choice = input(">>> ").lower()
    # Selection.
    while choice != "q":

        if choice == "c":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[choice]
            except IndexError:
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                drive = float(input("Drive how far? "))
                current_taxi.drive(drive)
                cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
                total_bill += cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")
        print("\n", MENU)
        choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()
