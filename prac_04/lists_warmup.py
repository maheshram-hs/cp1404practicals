"""
Warm up in list expressions.

Warm-Up. Created by Maheshram Shunmuganand, December 2021
"""


def main():
    """Warm up in lists."""
    numbers = [3, 1, 4, 1, 5, 9, 2]

    # numbers[0] == 3
    # numbers[-1] == 2
    # numbers[3] == 1
    # numbers[:-1] == 2
    # numbers[3:4] == [1, 4]
    # 5 in numbers == True
    # 7 in numbers == False
    # "3" in numbers == False
    # numbers + [6, 5, 3] == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    print(numbers[0] == 3)
    print(numbers[-1] == 2)
    print(numbers[3] == 1)
    print(numbers[:-1] == 2)  # Correct answer is [3, 1, 4, 1, 5, 9], That's, to -1.
    print(numbers[3:4] == [1, 4])  # Correct answer is [1].
    print(5 in numbers)  # True
    print(7 in numbers)  # False
    print("3" in numbers)  # False
    print(numbers + [6, 5, 3] == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3])

    print("\nCheck code for Python expressions to achieve the following:\n")
    print("Original List: ", numbers)

    # Answer 1.
    numbers[0] = "10"
    print("     Answer 1: ", numbers)

    # Answer 2.
    numbers[-1] = 1
    print("     Answer 2: ", numbers)

    # Answer 3.
    result = numbers[1:-1]
    print("     Answer 3: ", result)

    # Answer 4.
    print("     Answer 4: ", 9 in numbers)


if __name__ == "__main__":
    main()
