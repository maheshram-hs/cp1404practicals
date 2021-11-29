"""
Generates a password that matches the user chosen length and other requirements.

Automatic Password Generator. Created by Maheshram Shunmuganand, November 2021
"""
import random
import string

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Generate a password that matches the user chosen length and other requirements."""
    print("Automatic Password Generator")
    length = int(input("Enter the length of the password: "))
    print("Choose your password characteristics.")
    choice_upper_case = input("Upper Case (U/u): ")
    choice_lower_case = input("Lower Case (L/l): ")
    choice_numeric = input("Numeric (N/n): ")
    choice_special = input("Special Character (S/s): ")

    choice = choice_upper_case.upper() + choice_lower_case.upper() + choice_numeric.upper() + choice_special.upper()

    if choice_upper_case:
        ...
    elif choice_lower_case:
        ...
    elif choice_numeric:
        ...
    elif choice_special:
        ...

    word_format = ""
    for i in range(length):
        word_format += random.choice([random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase),
                                      random.choice(SPECIAL_CHARACTERS)])
    print(word_format)


if __name__ == "__main__":
    main()
