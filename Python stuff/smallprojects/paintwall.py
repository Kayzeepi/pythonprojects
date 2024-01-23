#Write your code below this line
import math
def paint_calc(height, width, cover):
    number_of_cans = (height*width)/5
    number_of_cans=math.ceil(number_of_cans)
    print(f"You'll need {number_of_cans} cans of paint.")





#above
#define a function called paint_calc() so the code below works

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)