print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")

a = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'").lower()
if a == "left":
    b = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.").lower()
    if b == "wait":
        c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door do you choose?:").lower()
        if c == "yellow":
            print("You found the treasure, you win!")
        if c == "red":
            print("It's a room full of fire. Game Over.")
        if c == "blue":
            print("You are drowned as the room full of water. Game Over.")
        else:
            print("You didn't choose to correct door, Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
