"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Convert data strings into lists and display."""
    data = get_data()
    print(data)
    subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_lists = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        list_of_lists.append(parts)
    input_file.close()
    return list_of_lists


def subject_details(lists):
    """Display subject details."""
    for element in lists:
        print("{} is thought by {:12} and has {:3} students".format(element[0], element[1], element[2]))


if __name__ == "__main__":
    main()
