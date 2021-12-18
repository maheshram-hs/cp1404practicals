"""
CP1404/CP5632 - Practical 02
Maheshram Shunmuganand - ASCII Table
Input a character and see the corresponding ASCII code, and vice versa.
"""

LOWER = 33
UPPER = 127


def main():
    """Convert character to ASCII code and vice versa."""
    # Convert character to ASCII code.
    character = input("\nEnter a character: ")
    print(f"The ASCII coder for {character} is {ord(character)}")

    # Convert ASCII code to character.
    ascii_code = get_number(LOWER, UPPER)
    print(f"The character for {ascii_code} is {chr(ascii_code)}")

    # ASCII table.
    # print("\nCode   Character\n")
    # for i in range(LOWER, UPPER + 1):
    #   print(f"{i:3} {chr(i):>8}")

    # ASCII table with columns.
    print("\n<<< ASCII Table >>>\n")
    columns = int(input("Number of columns: "))
    print()

    total_ascii = UPPER - LOWER + 1
    rows = total_ascii // columns

    ascii_number = LOWER
    for row in range(rows):
        for column in range(columns):
            print(f"{ascii_number:8} {chr(ascii_number):>2}", end="")
            ascii_number += 1
        print()

    continue_ascii = ascii_number
    for i in range(continue_ascii, UPPER + 1):
        print(f"{i:8} {chr(i):>2}", end="")
    print("\n")


def get_number(lower, upper):
    """Get input and Handle errors."""
    is_valid = False
    while not is_valid:
        try:
            user_input = int(input(f"Enter a number ({lower}-{upper}): "))
            while user_input > upper or user_input < lower:
                user_input = int(input(f"Enter a number ({lower}-{upper}): "))
            is_valid = True
        except ValueError or TypeError:
            print("Please enter a valid number! ")
    return user_input


if __name__ == "__main__":
    main()
