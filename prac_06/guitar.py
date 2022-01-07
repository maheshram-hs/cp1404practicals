"""
Class to store multiple values of guitar entities.

Guitar. Created by Maheshram Shunmuganand, December 2021
"""
from datetime import date

current_date = date.today()
current_year = current_date.year


class Guitar:
    """Store multiple values of guitar entities"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= 50
