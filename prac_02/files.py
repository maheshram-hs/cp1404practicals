"""
CP1404/CP5632 - Practical 02
Maheshram Shunmuganand - Files
Experience using different ways to read files.
"""


def main():
    """Different ways to read files."""
    NAME_FILE = "name.txt"

    # Asks the user for their name, then opens a file called "name.txt" and writes that name to it.
    out_file = open(NAME_FILE, 'w')
    name = input("Enter an name: ")
    out_file.write(name)
    out_file.close()

    # Open "name.txt" and reads the name and print it.
    load_file = open(NAME_FILE, 'r')
    name_is = load_file.read()   # Why should we .strip()?
    print("Your name is ", name_is)
    load_file.close()

    # Read only the first two numbers and adds them together then prints the result.
    numbers = open("numbers.txt", 'r')
    number_one = int(numbers.readline())
    number_two = int(numbers.readline())
    print(number_two + number_one)
    numbers.close()

    # Print the total for all lines in numbers.txt or a file with any number of numbers.
    numbers = open("numbers.txt", 'r')
    total = 0
    for line in numbers:
        total += int(line)
    print(total)
    numbers.close()


if __name__ == "__main__":
    main()
