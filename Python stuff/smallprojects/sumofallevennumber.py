target = int(input("Enter a number between 0 to 200:"))

#instructions write a program that calculates the usm of all the even numbers from 1 to input. so it adds from 2+4+6+ until the end of the number

even_sum=0

for num in range (1, target + 1):
    if num %2 == 0:
        even_sum += num

print(f"The total even number sum is: {even_sum}")