"""
Converts Celsius to Fahrenheit and vice versa.

Temperatures. Created by Maheshram Shunmuganand, November 2021
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":

        # Convert celsius to fahrenheit.
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))

        # Convert fahrenheit to celsius.
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))

        # Check for valid choice of option.
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you.")


def convert_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == "__main__":
    main()