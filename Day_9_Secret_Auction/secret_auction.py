import os


os.system("clear || cls")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\nWinner: {winner}\nWinner's bid: ${highest_bid}\n")


while not bidding_finished:
    name = input("\nWhat's your name? ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there other bidders? Enter 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system("clear || cls")