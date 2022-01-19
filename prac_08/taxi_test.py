"""
Program to test Ta class.

Test Taxi. Created by Maheshram Shunmuganand, January 2022
"""

from prac_08.taxi import Taxi


def main():

    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(f"{taxi}: ${taxi.get_fare()}")
    taxi.start_fare()
    print(f"{taxi}: ${taxi.get_fare()}")


if __name__ == '__main__':
    main()
