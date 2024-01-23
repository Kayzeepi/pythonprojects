student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = ["Outstanding"]
    elif score > 80 and score <= 90:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70 and score <= 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# student_grades[91,100] = "Outstanding"
# student_grades[81,90] = "Exceeds Expectations"
# student_grades[71,80] = "Acceptable"
# student_grades[0,70] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)









