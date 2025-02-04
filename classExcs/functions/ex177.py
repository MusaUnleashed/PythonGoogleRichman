def letter_grade(score):
    grade = None  # Initialize the grade variable
    if score >= 90:
        grade = "A"
    elif 80 <= score < 90:
        grade = "B"
    elif 70 <= score < 80:
        grade = "C"
    elif 60 <= score < 70:
        grade = "D"
    else:
        grade = "F"

    return grade  # Return the grade stored in the variable


assert letter_grade(100) == "A"
assert letter_grade(95) == "A"
assert letter_grade(90) == "A"
assert letter_grade(85) == "B"
assert letter_grade(80) == "B"
assert letter_grade(79.5) == "C"
assert letter_grade(72) == "C"
assert letter_grade(70) == "C"
assert letter_grade(69) == "D"
assert letter_grade(60) == "D"
assert letter_grade(59) == "F"
assert letter_grade(10) == "F"
assert letter_grade(1) == "F"
assert letter_grade(0) == "F"
print("OK")
