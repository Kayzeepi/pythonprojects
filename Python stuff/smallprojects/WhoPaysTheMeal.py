names = ["Eugene" , "Aaron", "Vanessa", "Emerie", "Carina"]

import random

num_items = len(names) #for the loop random_choice as we are not certain how big your list is 
#so using this can future proof your code and list starts by 0 so using 0, then num_items -1 will be correct

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
