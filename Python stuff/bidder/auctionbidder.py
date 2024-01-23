from replit import clear
from artbidder import logo
#HINT: You can call clear() to clear the output in the console.


bidders = {}

def find_highest_bidder(bidding_record):
    high_bidname=""
    high_bid = 0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>high_bid:
            high_bid=bid_amount
            high_bidname=bidder
    print(f"The winner is {high_bidname} with a bid of ${high_bid}!!!!!!!")

  

game_end=True
while game_end:
    print(logo)
    print("Welcome to the secret auction program.")
    name=input("What is your name?:")
    bidamount=int(input("What's your bid?: $"))
    bidders[name] = bidamount ## add inputs into list

    result=input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if result == "no":
        game_end=False
        find_highest_bidder(bidders)
    elif result == "yes":
        clear()

# for bidder in bidding_record:
#     amount = bidding_record[bidder]
#     if amount > high_bid:
#         high_bidname = bidder
#         high_bid = amount

