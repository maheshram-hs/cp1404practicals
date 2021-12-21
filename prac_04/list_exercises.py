"""
Basic list operations.

List Exercises. Created ny Maheshram Shunmuganand, December 2021
"""


def main():
    """Basic list operations."""
    numbers = []
    index = 1
    try:
        number = int(input(f"Number {index}: "))
        if number >= 0:
            while number >= 0:
                index += 1
                number = int(input(f"Number {index}: "))
                if number < 0:
                    break
                numbers.append(number)

            # Print output.
            print(f"The first number: {numbers[0]}")
            print(f"The last number: {numbers[-1]}")
            print(f"The smallest number: {min(numbers)}")
            print(f"The largest number: {max(numbers)}")
            print(f"The average of the numbers is {sum(numbers) / len(numbers):.0f}")

        print("Thank you.")

    except ValueError:
        print("Invalid input.")

    # Check username.
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Enter username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
