"""
Program to test Guitar class.

Guitar Test. Created by Maheshram Shunmuganand, December 2021
"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2013, 17945.90)

    print(f"{guitar.name} get_age() - Expected 95. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 5. Got {other.get_age()}")
    print("")

    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


if __name__ == '__main__':
    main()
