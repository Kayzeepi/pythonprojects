# student_heights = input("Input student heights like this in CM '156 178 139 149 159 168':").split()
# for n in range (0,len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_height=0
# for height in student_heights:
#     total_height += height
# print(f"Total height = {total_height}")

# total_student=0

# for student in student_heights:
#     total_student += 1
# print(f"Total students = {total_student}")

# average_height = round(total_height/total_student)
# print(f"Average height = {average_height}")

#Instructions Input a python list of student heights and give an output of total_Height / total_students / average_height using loop and list
#provided code

student_heights = input("Input student heights like this in CM '156 178 139 149 159 168':").split()
for n in range (0,len(student_heights)):
     student_heights[n] = int(student_heights[n])

#add on below