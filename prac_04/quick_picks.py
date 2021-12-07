"""
Generated random lottery tickets.

Quick Pick. Created by Maheshram Shunmuganand, December 2021
"""
import random

MIN_VALUE = 1
MAX_VALUE = 45
LENGTH = 6


def main():
    """Generate lottery ticket"""
    quick_picks = int(input("How many quick picks? "))
    # Handel input error.
    while quick_picks <= 0:
        print("Invalid input, number must be more than 0.")
        quick_picks = int(input("How many quick picks? "))

    # Generate lottery tickets.
    for columns in range(quick_picks):
        values = []

        for row in range(LENGTH):
            number = random.randint(MIN_VALUE, MAX_VALUE)

            # Look to not generate any repeated number in a row.
            while number in values:
                number = random.randint(MIN_VALUE, MAX_VALUE)

            values.append(number)

        # Sorting and printing the output.
        values.sort()
        print(" ".join("{:2}".format(value) for value in values))


if __name__ == '__main__':
    main()
