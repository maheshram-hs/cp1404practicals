"""
Class to store data about each language in their respective fields.

class: Programming Language. Created by Maheshram Shunmuganand, December 2021
"""


class ProgrammingLanguage:
    """Store language in their fields."""

    def __init__(self, field="", typing="", reflection="", year=0):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        if self.typing == "Static":
            return False
        else:
            return True
