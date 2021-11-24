"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $ "))

# Repeatedly asks for the user's sales and print the bonus until they enter a negative number.
while sales >= 0:

    # Calculate sales bonus.
    if sales < 1000:
        user_bonus = sales * 0.10
    elif sales >= 1000:
        user_bonus = sales * 0.15

    # Output statements.
    print("Your bonus is: ", user_bonus)
    print("To stop, please enter a negative number.")

    sales = float(input("Enter sales: $ "))

print("Thank you.")
