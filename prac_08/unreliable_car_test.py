"""
Test class UnreliableCar and show the difference between a reliable care and vice versa.

Unreliable Car Test. Created by Maheshram, January 2022
"""

from prac_08.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class"""
    taxi_one = UnreliableCar("Taxi Good", 100, 97)
    taxi_two = UnreliableCar("Taxi Bad", 100, 49)

    for i in range(1, 20):
        print(f"{taxi_one.name} drove {taxi_one.drive(i)}")
        print(f"{taxi_two.name} drove {taxi_two.drive(i)}")

    print(f"\n{taxi_one}\n{taxi_two}")


if __name__ == '__main__':
    main()
