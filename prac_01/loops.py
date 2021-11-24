"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Loops
Program to illustrate different types of Loops
"""

# Loop odd numbers between 1 and 20.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a) Count in 10s from 0 to 100.
for i in range(0, 110, 10):
    print(i, end=" ")
print()

# b) Count down from 20 to 1.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c) Print n stars.
star_count = int(input("Number of stars: "))
for i in range(star_count):
    print("*", end="")

# d) Print n lines of increasing stars.
for i in range(star_count + 1):
    print("*" * i)
