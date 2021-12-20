"""
Program that simulates a population of gophers over a ten-year period.

GPS (Gopher Population Simulator). Created by Maheshram Shunmuganand, December 2021
"""

import random

G_BORN_10 = 0.1
G_BORN_20 = 0.2
G_BYE_25 = 0.25
G_BYE_5 = 0.05
INITIAL_GOPHERS = 1000


def main():
    """..."""
    print("Welcome to the Gopher Population Simulator!")
    gophers = INITIAL_GOPHERS
    new_gophers = 0
    bye_gophers = 0
    year_counter = 1
    print("Starting population: ", INITIAL_GOPHERS)
    print("Year 1\n")

    for i in range(9):
        year_counter += 1

        if random.randint(0, 1) == 1:
            new_gophers = random.uniform(0, G_BORN_10)
        else:
            new_gophers = random.uniform(0, G_BORN_20)

        if random.randint(0, 1) == 0:
            bye_gophers = random.uniform(0, G_BYE_5)
        else:
            bye_gophers = random.uniform(0, G_BYE_25)

        gophers = gophers + (gophers * new_gophers)
        gophers_born = gophers * new_gophers

        gophers = gophers + (gophers * bye_gophers)
        gophers_died = gophers * bye_gophers

        print(f"{gophers_born:.0f} gophers were born. {gophers_died:.0f} died.")
        print(f"Population: {gophers:.0f}")
        print("Year ", year_counter)
        print("")


if __name__ == '__main__':
    main()
