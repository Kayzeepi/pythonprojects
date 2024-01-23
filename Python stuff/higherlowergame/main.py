from art import logo, vs
from game_data import data
import random
from replit import clear

def get_random_account ():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account ["description"]
    country = account ["country"]

    return f"{name}, a {description}, from {country}"

def compare (guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():        
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a==account_b:
            account_b = get_random_account()
        print(logo)
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Compare B: {format_data(account_b)}")
        guess=input("Who has more followers? Type 'A' or 'B':").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = compare(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        
        if is_correct:
            score +=1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

game()