"""
Program to test the class ProgrammingLanguage.

Languages. Created by Maheshram Shunmuganand, December 2021
"""

from prac_06.programming_language import ProgrammingLanguage  # Don't forget to add the file name after prac_06...


def main():
    """Test the class ProgrammingLanguage"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    # print(ruby) # Testing.
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for i in languages:
        if i.is_dynamic():
            print(i.field)


if __name__ == '__main__':
    main()
