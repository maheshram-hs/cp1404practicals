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
    # Error Handling.
    try:
        ascii_code = int(input(f"\nEnter a number between {LOWER} and {UPPER}: "))
    except ValueError:
        ascii_code = int(input(f"\nEnter a VALID NUMBER between {LOWER} and {UPPER}: "))
    while ascii_code < LOWER or ascii_code > UPPER:
        ascii_code = int(input(f"Enter a number BETWEEN {LOWER} and {UPPER}: "))
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


if __name__ == "__main__":
    main()
