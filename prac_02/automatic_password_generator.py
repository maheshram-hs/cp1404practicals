"""
Generates a password that matches the user chosen length and other requirements.

Automatic Password Generator. Created by Maheshram Shunmuganand, November 2021
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
        UPPER_CHAR_REQUIRED = True
    else:
        UPPER_CHAR_REQUIRED = False
    if choice_lower_case.upper() == "Y":
        word_format += "L"
        LOWER_CHAR_REQUIRED = True
    else:
        LOWER_CHAR_REQUIRED = False
    if choice_numeric.upper() == "Y":
        word_format += "N"
        NUMERIC_REQUIRED = True
    else:
        NUMERIC_REQUIRED = False
    if choice_special.upper() == "Y":
        word_format += "S"
        SPECIAL_CHARS_REQUIRED = True
    else:
        SPECIAL_CHARS_REQUIRED = False

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
    print()

    while not is_valid_password(password, length, UPPER_CHAR_REQUIRED, LOWER_CHAR_REQUIRED, NUMERIC_REQUIRED,
                                SPECIAL_CHARS_REQUIRED):
        print("Invalid password!")
        password = input("Enter password:  ")
    print("Your {}-character password is valid: {}".format(len(password), password))


def is_valid_password(password, length, UPPER_CHAR_REQUIRED, LOWER_CHAR_REQUIRED, NUMERIC_REQUIRED,
                      SPECIAL_CHARS_REQUIRED):
    """Determine if the automatically generated password is valid."""
    if len(password) < length or len(password) > length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # Count each kind of character (use str methods like isdigit).
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    # If any of the counts are zero, return False.
    if UPPER_CHAR_REQUIRED:
        if count_upper == 0:
            return False
    if LOWER_CHAR_REQUIRED:
        if count_lower == 0:
            return False
    if NUMERIC_REQUIRED:
        if count_digit == 0:
            return False
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    # If we get here (without returning False), then the password must be valid.
    return True


if __name__ == "__main__":
    main()
