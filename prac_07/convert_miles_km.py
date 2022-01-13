"""
Program to convert miles to kilometers.

Miles to Kilometers Converter. Created by Maheshram Shunmuganand, January 2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'Maheshram Shunmuganand'
MILES_TO_KM = 1.609344

"""I did update my code by using the solutions to improve efficiency."""


class MilesConvert(App):
    message = StringProperty()

    def build(self):
        """App stuff..."""
        Window.size = (600, 420)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert(self, text):
        """Convert miles to kilometers."""
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_ud(self, ud, text):  # ud: up and down
        """Increment and decrement the miles."""
        miles = self.convert_to_number(text) + ud
        self.root.ids.user_input.text = f"{miles:.0f}"

    def update_result(self, miles):
        self.message = f"{miles * MILES_TO_KM:.3f}"

    def convert_to_number(self, text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConvert().run()
