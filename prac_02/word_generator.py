"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
alphabet = string.ascii_letters

# word_format = input("Enter word format: ").lower()  # "ccvcvvc"

word_format = ""
for i in range(random.randint(1, 12)):
    word_format += random.choice(["#", "%", random.choice(alphabet).lower()])  # Now that's truly random ;)

word = ""
for kind in word_format:
    if kind == "#":
        word += random.choice(CONSONANTS)
    elif kind == "%":
        word += random.choice(VOWELS)
    else:
        word += kind

print(word)
