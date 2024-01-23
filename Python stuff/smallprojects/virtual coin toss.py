import random

print("This is a virtual coin toss program which tells you if it is Heads or Tails. ")

random_number = random.randint(0, 1)
if random_number == 0:
    print("This is Heads")
else:
    print("This is Tails")
