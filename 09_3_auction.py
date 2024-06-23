import os

bidder = {}
highest_bidder = ""
highest_bid = 0
another_bidder = True

print("Welcome to the secret auction program.")

while another_bidder:
  name = input("What is your name?: ").capitalize()
  bid = int(input("What is your bid: $"))
  another = input("Are there any other bidders? (y/n)").lower()

  bidder[name] = bid

  if another != "y":
    another_bidder = False
  else:
    os.system('cls' if os.name == 'nt' else 'clear')

for i in bidder:
  if bidder[i] > highest_bid:
    highest_bidder = i
    highest_bid = bidder[i]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")