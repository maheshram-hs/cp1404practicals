"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Sequences
Program that would allow primary school students to learn about various number sequences.
"""
import math

MENU = """i.   To show the even numbers from x to y.     > (E/e)
ii.  To show the odd numbers from x to y.      > (O/o)
iii. To show the squares from x to y.          > (S/s)
iv.  To change 'x' and 'y' values.             > (C/c)
v.   To exit the program.                      > (Q/q)"""

print("\n{:-<18} Number Sequences {:-<18}\n".format("", ""))

# Get 'x' and 'y' values from the user.
# Handling input error.
while True:
    try:
        x_value = input("Enter 'x' value: ")
        x_value = int(x_value)
        break
    except ValueError:
        print("Invalid input, please enter an valid integer.")
print("Valid 'x' input saved, thank you.")
# Handling input error.
while True:
    try:
        y_value = input("Enter 'y' value: ")
        y_value = int(y_value)
        break
    except ValueError:
        print("Invalid input, please enter an valid integer.")
print("Valid 'y' input saved, thank you.")

# Print menu and get input from the user.
print("\n{:*<24} {} {:*<24}\n{}".format("", "MENU", "", MENU))
print("{:*<54}".format(""))
choice = input(">>> ")
print("")

while choice.upper() != "Q":

    # Print all even numbers from given range.
    if choice.upper() == "E":
        print("\n{:-<54}".format(""))
        print("Even numbers from {} to {} are :-".format(x_value, y_value))
        for i in range(x_value, y_value + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print("\n{:-<54}\n".format(""))

    # Print all odd numbers from given range.
    elif choice.upper() == "O":
        print("\n{:-<54}".format(""))
        print("Odd numbers from {} to {} are :-".format(x_value, y_value))
        for i in range(x_value, y_value + 1):
            if i % 2 != 0:
                print(i, end=" ")
        print("\n{:-<54}\n".format(""))

    # Print all square numbers from given range.
    elif choice.upper() == "S":
        print("\n{:-<54}".format(""))
        print("Square numbers from {} to {} are :-".format(x_value, y_value))
        for i in range(x_value, y_value + 1):
            root = math.sqrt(i)
            if int(root + 0.5) ** 2 == i:
                print(i, end=" ")
        print("\n{:-<54}\n".format(""))

    # Change 'x' and 'y' value.
    elif choice.upper() == "C":
        # Handling input error.
        while True:
            try:
                x_value = input("Enter the new 'x' value: ")
                x_value = int(x_value)
                break
            except ValueError:
                print("Invalid input, please enter an valid integer.")
        print("Valid 'x' input saved, thank you.")
        # Handling input error.
        while True:
            try:
                y_value = input("Enter the new 'y' value: ")
                y_value = int(y_value)
                break
            except ValueError:
                print("Invalid input, please enter an valid integer.")
        print("Valid 'y' input saved, thank you.")

        print("\n{:-<54}".format(""))
        print("The new 'x' and 'y' value has been saved.")
        print("{:-<54}\n".format(""))

    # Repeat the menu display and prompt.
    print("{:*<24} {} {:*<24}\n{}".format("", "MENU", "", MENU))
    print("{:*<54}".format(""))
    choice = input(">>> ")
    print("")

print("{: <18} Number Sequences {: <18}".format("", ""))
print("{: <21} Thank you. {: <21}".format("", ""))
