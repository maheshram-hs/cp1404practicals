"""
Get user for their score and print the result.

Broken Score. Created by Maheshram Shunmuganand, November 2021
"""


def main():
    """Get user for their score and print the result."""
    score = float(input("Enter score: "))
    print(score_result(score))


def score_result(score):
    """Generate result for given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == "__main__":
    main()
