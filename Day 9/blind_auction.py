from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
bidders = {}
bidder_name = input("What is your name?: ")
bid_amount = int(input("What is your bid?: $"))
bid_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
highest_bid = 0
def add_bidders_info(bid_record):
  for bidder in bidders:
      if bidders[bidder] > highest_bid:
        highest_bid = bidders[bidder]
  print(f"The winner is {bidder} with a bid of ${highest_bid}")
  
more_bidders = True
while more_bidders:
  clear()
  bidder_name = input("What is your name?: ")
  bid_amount = int(input("What is your bid?: $"))
  bidders[bidder_name] = bid_amount
  bid_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if bid_continue == "no":
    more_bidders = False
    add_bidders_info(bid_record=bidders)