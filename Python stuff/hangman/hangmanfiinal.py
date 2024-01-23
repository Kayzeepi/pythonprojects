#Step 5
from replit import clear
import random
from hangman_art import *
from hangman_words import *

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"the WORD consist of {len(chosen_word)} letters")
    guess = input("Guess a letter: ").lower()

    clear()
    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            if display[position] == letter:
                print(f"You already guessed the letter {letter}")
                break
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"You guessed {guess}, Thats not in the word. You lose a life!\n Life remaining:{lives}")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'Pssst, the solution is {chosen_word}.')

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(f'Pssst, the solution is {chosen_word}.')

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])