# Bug: an error in a program that prevents the program from running as expected
# Function: a piece of code that you can easily call over and over again.
from replit import clear
from art import logo

tprint(logo)



# dictionary
bids= {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ''
    # bidding_record = {'Angela': 123, 'James':321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}.')


while not bidding_finished:
    name = input('What is your name?:')
    price = input('Your Bid:')
    bids[name] = price
    should_continue = input('Are there any other bidders? Type yes or no')
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear()
