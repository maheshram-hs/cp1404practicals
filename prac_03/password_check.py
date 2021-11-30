"""
Validate password for minimum length and print the password in asterisks.

Password Checker. Created by Maheshram Shunmuganand, November 2021
"""
MIN_LENGTH = 6


def main():
    """Check if password meets the minimum length and print the validated password in asterisks."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(word):
    """Print the parameter string in asterisks."""
    for char in word:   # print('*' * len(word))
        print("*", end="")


def get_password():
    """Get password from user and handle minimum length requirements."""
    password = input("Enter password: ")
    # Error handling.
    while len(password) < MIN_LENGTH:
        print(f"Your password must have a minimum of {MIN_LENGTH} characters.")
        password = input("Enter password: ")
    return password


if __name__ == "__main__":
    main()