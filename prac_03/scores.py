"""
Ask user for number of scores and generate that many random numbers (scores).

Scores. Created by Maheshram Shunmuganand, December 2021
"""
import random


def main():
    """Get number of scores and generate that many random scores."""
    num_of_scores = int(input("Enter number of scores: "))
    for i in range(1, num_of_scores + 1):
        score = random.randint(1, 100)
        result = score_result(score)
        print(f"{i}) {score} is {result}")


def score_result(score):
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