"""
Validate password for minimum length and print the password in asterisks.

Password Checker. Created by Maheshram Shunmuganand, November 2021
"""
MIN_LENGTH = 6


def main():
    """Check if password meets the minimum length and print the validated password in asterisks."""
    password = input("Enter password: ")

    # Error handling.
    while len(password) < MIN_LENGTH:
        print(f"Your password must have a minimum of {MIN_LENGTH} characters.")
        password = input("Enter password: ")

    # Print in asterisks.
    for char in password:
        print("*", end="")


if __name__ == "__main__":
    main()