"""
Program to takes two lists, and returns the list that contains the sum of elements.

Concatenate Lists. Created by Maheshram Shunmuganand, December 2021
"""


def main():
    list_one = [1, 20, 0, 4]
    list_two = [2, 2, 2]
    print(add_memberwise(list_one, list_two))


def add_memberwise(a, b):
    """
    For example:
    add_memberwise([1, 2, 3], [4, 5, 6]) would return [5, 7, 9] and
    add_memberwise([1, 2, 3], [1, 2, 3, 4]) would return [2, 4, 6, 4]
    """

    iter_len = len(a) - (len(b) - 1)

    for j in range(len(a), 0, -1):

        if j - iter_len < 0:
            break
        else:
            a[j - 1] = a[j - 1] + b[j - iter_len]
    return a


if __name__ == '__main__':
    main()
