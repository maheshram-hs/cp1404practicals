"""
Program to use the Guitar class.

Guitars. Created by Maheshram Shunmuganand, January 2022
"""

from prac_06.guitar import Guitar


def main():
    """Play the guitars (not really;)"""
    print("My guitars!")
    name = input("Name: ")
    guitars = []
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(guitar, " added.")
        name = input("\nName: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("\n... snip ...\n\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} (vintage)")
            else:
                print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
    else:
        print("\nNo guitars :( Quick, go and buy one!")


if __name__ == '__main__':
    main()
