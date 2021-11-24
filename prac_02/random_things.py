"""
CP1404/CP5632 - Practical 02
Maheshram Shunmuganand - Random Things
Three different versions of code to generate a random Boolean (True or False).
"""
import random


def main():
    """Generate different versions of code to generate a random Boolean."""
    # I found most of these methods off the internet, so
    # am not sure if this what I am supposed to do.

    # Method one.
    choice_1 = random.choice([True, False])
    print(choice_1)

    # Method two.
    if random.randint(1, 2) == 1:
        print("True")
    else:
        print("False")

    # Method three.
    choice_3 = random.getrandbits(1)
    print(choice_3)

    # Method four.
    choice_4 = bool(random.getrandbits(1))
    print(choice_4)

    # Method five.
    choice_5 = not random.getrandbits(1)
    print(choice_5)

    # Method seven.
    choice_7 = not not random.getrandbits(1)
    print(choice_7)


if __name__ == "__main__":
    main()