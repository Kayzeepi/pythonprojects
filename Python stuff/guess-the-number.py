#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 6

def difficulty():
    level = input ("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS

def compare (answer, guess, turns):
    if answer == guess:
        print(f"Correct! {answer}")
    elif answer > guess:
        print("Too high ")
        return turns - 1
    elif answer < guess:
        print("Too low")
        return turns - 1 

def game():        
    answer = random.randint(1,100)
    guess = 0
    print(logo)
    print(answer)
    print("Welcome to the Number Guessing game!\nI'm thinking of a number between 1 and 100.")
    turns = difficulty()

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int (input("Make a guess:"))

        turns = compare(guess, answer, turns)

        if turns == 0:
            print("You've run out of turns. you lose. ")
            return

game()