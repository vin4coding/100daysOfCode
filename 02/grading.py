# Dict of student scores
student_score = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Should calculate grading for the students;
# Initializing empty dict for grades.
student_grades = {}
for grade in student_score:
    if student_score[grade] in range(91, 100):
        student_grades[grade] = "Outstanding"
    elif student_score[grade] in range(81, 90):
        student_grades[grade] = "Exceeds Expectations"
    elif student_score[grade] in range(71, 80):
        student_grades[grade] = "Acceptable"
    elif student_score[grade] <= 70:
        student_grades[grade] = "Fail"

print(student_grades)
