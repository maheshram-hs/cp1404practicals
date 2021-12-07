"""
Basic list operations.

List Exercises. Created ny Maheshram Shunmuganand, December 2021
"""


def main():
    """Basic list operations."""
    numbers = []
    for i in range(1, 6):
        number = int(input(f"Number {i}: "))
        numbers.append(number)

    # Output
    print(f"The first number: {numbers[0]}")
    print(f"The last number: {numbers[-1]}")
    print(f"The smallest number: {min(numbers)}")
    print(f"The largest number: {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")


if __name__ == "__main__":
    main()