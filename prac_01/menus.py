"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Menus
Making menus by combining looping with selection.
"""

MENU = """(H)ello
(G)oodbye
(Q)uit"""

name = input("Enter name: ")

print(MENU)
choice = input(">>>")

# Repeat the program until the user quits.
while choice.upper() != "Q":

    # Output the selection.
    if choice.upper() == "H":
        print("Hello ", name.title())
    elif choice.upper() == "G":
        print("Goodbye ", name.title())
    else:
        print("Invalid choice")

    # Repeat the menu display and prompt.
    print(MENU)
    choice = input(">>>")

print("Finished.")
