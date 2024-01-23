#Write a program that auto prints the solutions to the fizzbuzz game

#your program should print each number from 1 to 100 in turn and include the number 100

#when the number is divisible by 3 then instead of printing the number it should print "Fizz".

#when the number is divisible by 5, then instead of printing the number it should print "Buzz".

#if it is both divisible by both 3 and 5 then it should print FizzBuzz

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("Fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)      
    

##INTERVIEW QUESTION SIOL EASY
         
