"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Temperatures
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)
choice = input(">>> ").upper()
while choice != "Q":

    # Convert celsius to fahrenheit.
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))

    # Convert fahrenheit to celsius.
    elif choice == "F":
        fahrenheit = float(input("fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))

    # Check for valid choice of option.
    else:
        print("Invalid option")

    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
