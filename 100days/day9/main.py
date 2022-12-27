import os
os.system('cls')

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    hightest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > hightest_bid:
            hightest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${hightest_bid}")

while not bidding_finished:
    name = input("What's your name?\n")
    price = int(input("What is your bid?:\n$"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'?\n")
    if should_continue == 'yes':
        os.system('cls')
        print(logo)
    else:
        bidding_finished = True
        os.system('cls')
        print(logo)
        find_highest_bidder(bids)
