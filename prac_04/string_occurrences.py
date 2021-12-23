"""program that gets an indefinite set of strings, then prints all of the strings that were entered more
than once.

String Occurrences. Created by Maheshram Shunmuganand, December 2021
"""


def main():
    """Gets an indefinite set of strings and print occurrences."""
    strings = []
    occurrences = []
    string_input = input("Enter string: ")

    while string_input != "":
        strings.append(string_input)
        string_input = input("Enter string: ")

    for i in strings:
        if i not in occurrences:
            occurrences.append(i)

    flag = 0
    for i in range(0, len(occurrences)):
        if strings.count(occurrences[i]) > 1:
            print(f"{occurrences[i]} is: {strings.count(occurrences[i])}")
        else:
            print("No repeated strings entered")
            flag = 1
        if flag == 1:
            break


if __name__ == '__main__':
    main()
