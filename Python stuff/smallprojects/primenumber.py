#write your code
def prime_checker(number, flag=False):
    if number ==1:
        print(f"{number} is not a prime number")
    elif number>1:
        for i in range(2,number):
            if (number%i)==0:
                flag=True
                break
        
        if flag is True:
            print(f"{number} is not a prime number")
        else:
            print(f"{number}, is a prime number")






#write your code above
n=int(input()) #check this number
prime_checker(number=n)