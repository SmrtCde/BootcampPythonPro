from replit import clear

from PythonDictionaries.SecretAuctionArt import logo

######################################################################################

## take-aways
"""
--do not need to build dictionary/lists/nested BEFORE you send/add data to it
--input().lower was throwing an error, and not allowing the while look to exit

"""

bids = {}
bid_finish = 1

def high_bid(bidding_record):
  highest = 0
  winner = ""
  for bidder in bidding_record:
    bid_amt = bidding_record[bidder]
    if bid_amt > highest:
      highest = bid_amt
      winner = bidder
  print(f"\nWinner is {winner} with a bid of {highest}.")


while bid_finish == 1:
  print(logo)
  name = input("\n\nWhat is your name?: ")
  price = int(input("\nWhat's your bid?: "))
  bids[name] = price
  cont = input("\nAre there any add'l bidders? Type yes or no: ")
  if cont.lower() == "no":
    bid_finish = 0
    high_bid(bids)
  else:
    clear()
