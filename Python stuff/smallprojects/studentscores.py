#Instructions write a program that calculates the highest score from a list of scores

#student_ score not allowed to use max or min functions

#example input 71 78 28 39 59 69 99

#output "The highest score in the class is: 91"

student_scores = input("Input the student scores: ").split()
for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

high_score=0

for score in student_scores:
    if score>high_score:
        high_score = score
        
print(f"The highest score in the class is: {high_score}")
        