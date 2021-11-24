"""
CP1404/CP5632 - Practical 01
Maheshram Shunmuganand - Broken Score
Broken program to determine score status
"""

score = float(input("Enter score: "))

# Attempt 2

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")

# Attempt 1

"""# Check if score is invalid.
while score >= 0 and score < 101:

    # Check if score is bad, passable or excellent.
    if score >= 90 and score <= 100:
        print("Excellent")
        score = float(input("Enter score: "))
    elif score >= 50 and score < 90:
        print("Passable")
        score = float(input("Enter score: "))
    else:
        print("Bad")
        score = float(input("Enter score: "))

print("Invalid score")
score = float(input("Enter score: "))
"""

# Attempt 1.2

# Change 'START' to 'True' inorder to start the loop.
# Also, comment out attempt 2.
START = False

while START:

    if score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    elif score >= 90:
        print("Excellent")
        score = float(input("Enter score: "))
    elif score >= 50:
        print("Passable")
        score = float(input("Enter score: "))
    else:
        print("Bad")
        score = float(input("Enter score: "))
