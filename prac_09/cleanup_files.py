"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os
import string


def main():
    """Demo os module functions."""
    # file_name = "Away In A Manger.txt"
    # file_name = "Silent_Night.txt"
    # file_name = "O little town of bethlehem.TXT"
    file_name = "ItIsWell (oh my soul).txt"
    print(get_fixed_filename(file_name))


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

    filename = filename.replace(" ", "_").replace(".TXT", ".txt")

    new_name = ""
    previous_char = ""
    for i, char in enumerate(filename):
        if char.isupper() and i != 0 and previous_char != "_":
            new_name += "_"

        if char.islower() and previous_char in SPECIAL_CHARACTERS:
            new_name += char.upper()
            previous_char = char
            continue

        new_name += char
        previous_char = char

    new_name = new_name.replace(".Txt", ".txt")

    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Add a loop to rename the files
        for filename in filenames:
            old_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("Renaming {} to {}".format(old_name, new_name))
            # os.rename(old_name, new_name)


main()
# demo_walk()
