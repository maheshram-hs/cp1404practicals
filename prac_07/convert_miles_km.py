"""
Program to convert miles to kilometers.

Miles to Kilometers Converter. Created by Maheshram Shunmuganand, January 2022
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Maheshram Shunmuganand'


class MilesConvert(App):
    def build(self):
        Window.size = (600, 420)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


MilesConvert().run()
