"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Shop Calculator
Program that would quickly work out the total price for a number of items, each with different prices.
"""

total_price = 0
print("")
number_of_items = int(input("Number of items: "))

# Validate input.
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
print("----------------------")

# Ask for...and computes the total price of items.
for i in range(number_of_items):
    count = i + 1
    price = float(input("Price of item {}: ".format(i + 1)))
    total_price += price
print("------------------------------------")

# Apply 10% discount.
if total_price > 100:
    discounted_price = total_price * 0.30
    total_price -= discounted_price

print("Total price for {} items is ${:.2f}".format(count, total_price))
print("------------------------------------")
