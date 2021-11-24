"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


# 1. ValueError occurs when the user doesn't enter the input in the expected datatype.
# 2. ZeroDivisionError will occur when the user attempts to divide the numerator by 0.
# 3. Yes, just add in while loop to repeat until the user enters a non-zero value.

def main():
    """Divide two user input values and handle exceptions."""
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        while denominator == 0:
            print("The denominator shouldn't be 0, try another one. ")
            denominator = int(input("Enter the denominator: "))

        fraction = numerator / denominator
        print(f"{fraction:.2f}")
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


if __name__ == "__main__":
    main()
