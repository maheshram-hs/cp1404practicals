"""
Generates a password that matches the user chosen length and other requirements.

Automaticly Password Generator. Created by Maheshram Shunmuganand, November 2021
"""
import random
import string

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Generate a password that matches the user chosen length and other requirements."""
    print("*** Automatic Password Generator ***\n")
    length = int(input("Enter the length of the password: "))
    print("Choose your password characteristics by entering (Y)es or (N)o for the following options.")
    choice_upper_case = input("Upper Case (Y/N): ")
    choice_lower_case = input("Lower Case (Y/N): ")
    choice_numeric = input("Numeric (Y/N): ")
    choice_special = input("Special Character (Y/N): ")

    # Make the word format.
    word_format = ""
    if choice_upper_case.upper() == "Y":
        word_format += "U"
    if choice_lower_case.upper() == "Y":
        word_format += "L"
    if choice_numeric.upper() == "Y":
        word_format += "N"
    if choice_special.upper() == "Y":
        word_format += "S"

    # Generating the random password according to the word format.
    password = ""
    count = 0
    flag = 0
    for i in range(length):
        for char in word_format:

            if count == length:
                # To make it run more efficiently.
                flag = 1
                break
            count += 1

            # Generating the random password.
            if char == "U":
                password += random.choice(string.ascii_uppercase)
            elif char == "L":
                password += random.choice(string.ascii_lowercase)
            elif char == "N":
                password += str(random.randint(0, 9))
            elif char == "S":
                password += random.choice(SPECIAL_CHARACTERS)

        # To stop the outer for loop from running unnecessary.
        if flag == 1:
            break

    print("Your randomly generated password is: ", password)
    print(len(password))


if __name__ == "__main__":
    main()
