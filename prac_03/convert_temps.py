"""
Read values in as Fahrenheit and write the converted Celsius to file.

Convert Temperatures. Created by Maheshram Shunmuganand, December 2021
"""
import random


def main():
    """Read values in as Fahrenheit and write the converted Celsius values."""
    in_file = open("temps_input.txt", 'r')
    out_file = open("temps_output.txt", 'w')

    # Generating random number.
    # for i in range(15):
    # print(random.uniform(-200, 200))

    for line in in_file:
        temp = convert_to_celsius(float(line))
        print(temp, file=out_file)

    in_file.close()
    out_file.close()


def convert_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


if __name__ == "__main__":
    main()
