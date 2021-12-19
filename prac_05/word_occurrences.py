"""
Program to count the occurrences of words in a string.

Word Occurrences. Created by Maheshram Shunmuganand, December 2021
"""


def main():
    """Get string from user and count the occurrences of words."""
    sentence = input("Text: ")
    words = sentence.split()
    occurrences = {}
    for word in words:
        occurrences[word] = occurrences.get(word, 0) + 1

    # Sorting the keys. Eg: ['a', 'collection', 'fun', 'is', 'it', 'nice', 'of', 'thing', 'this', 'words']
    words = list(occurrences.keys())
    words.sort()

    # Find the longest word in the list to leave that many spaces.
    length = max(len(word) for word in words)

    # Printing the sorted keys and their values.
    for word in words:
        print(f"{word:<{length}} : {occurrences[word]}")


if __name__ == '__main__':
    main()
