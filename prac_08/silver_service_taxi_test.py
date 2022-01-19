"""
Program to test the SilverServiceTaxi class.

Silver Service Taxi Test. Created by Maheshram Shunmuganand, January 2022
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServicesTaxi class."""
    test_taxi = SilverServiceTaxi("Aston Martin DB11 V12 Vantage", 100, 2)  # Noo, not a 2!
    test_taxi.drive(18)
    print(test_taxi)
    print(f"The fare is: {test_taxi.get_fare():.2f}")  # I really like f strings!
    test_taxi.add_fuel(18)  # Just checking if the add_duel will work here...
    print(test_taxi)  # Good, it does!


if __name__ == '__main__':
    main()
