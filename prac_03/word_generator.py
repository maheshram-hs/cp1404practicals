"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    """..."""
    word_format = input("Enter word format: ").lower()  # Example input: "ccvcvvc"
    while not is_valid_format(word_format):
        print("Invalid word format, Example input: ccvcvvc")
        word_format = input("Enter word format: ").lower()

    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":  # Use else-statement when error checking function is added.
            word += random.choice(VOWELS)
    print(word)


def is_valid_format(sequence):
    for char in sequence:
        if char == "c" or char == "v":
            pass
        else:
            return False
    return True


if __name__ == '__main__':
    main()
