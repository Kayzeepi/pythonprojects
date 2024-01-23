#Easy level output
#abcD!@#123

#hard level output
#A!1B#2D%3


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
# for char in range (1,nr_letters+1):
#     password += random.choice(letters)
    
# for sym in range (1,nr_symbols+1):
#     password += random.choice(symbols)

# for num in range (1, nr_numbers+1):
#     password += random.choice(numbers)

# print(password)

# encrypt_pw = ''.join(random.sample(password, len(password)))  ## 1 sentence for string storage

# print(encrypt_pw) 

password = []
for char in range (1,nr_letters+1):
     password += random.choice(letters)
   
for sym in range (1,nr_symbols+1):
     password += random.choice(symbols)

for num in range (1, nr_numbers+1):
     password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password) ##Shuffle the password result

encrypt_password = ""
for char in password:
     encrypt_password +=char #add 1 character at a time

print(f"Your password is: {encrypt_password}")