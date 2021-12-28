"""
Class to store multiple values of guitar entities.

Guitar. Created by Maheshram Shunmuganand, December 2021
"""


class Guitar:
    """Store multiple values of guitar entities"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year} : S{self.cost:.,2f})"
