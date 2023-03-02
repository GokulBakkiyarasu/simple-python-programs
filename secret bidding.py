from replit import clear
from art import logo
bidders={}
should_continue=True
while should_continue:
  print(logo)
  name=input("Enter your name please: ")
  bid=int(input("Enter your bid ammount: $"))
  bidders[name]=bid
  clear()
  continue1=input("Please enter 'yes' to add another bidder or 'no' to show the bidding results: ")
  if continue1=="no":
    should_continue=False
def bid_calculation():
  amount_list=[]
  for keys in bidders:
    amount_list.append(bidders[keys])
  highest_bid=int(max(amount_list))
  for key in bidders:
    if bidders[key]==highest_bid:
      highest_bidder_name=key
  print(f"The highest bidder is {highest_bidder_name},with a bid amount of ${highest_bid}")
  print("Congrats for winning the BID!!!\nThank You.....!")

bid_calculation()
