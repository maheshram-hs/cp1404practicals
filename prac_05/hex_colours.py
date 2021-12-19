"""
Get colour name from user and print its HEX code.

Hex Colours. Created by Maheshram Shunmuganand, December 2021
"""

COLOURS = {"0048ba": "Absolute Zero", "b0bf1a": "Acid Green", "f0f8ff": "AliceBlue", "e32636": "Alizarin crimson",
           "e52b50": "Amaranth", "ffbf00": "Amber", "9966cc": "Amethyst", "faebd7": "AntiqueWhite",
           "ffefdb": "AntiqueWhite1", "eedfcc": "AntiqueWhite2", "cdc0b0": "AntiqueWhite3"}

NEW_COLOURS = dict([(value, key) for key, value in COLOURS.items()])


def main():
    """Get colour name from user and print its name."""
    colour_name = input("Enter colour name: ")
    while colour_name != "":
        print("Colour Code: ", NEW_COLOURS.get(colour_name))
        colour_name = input("Enter colour name: ")


if __name__ == '__main__':
    main()
