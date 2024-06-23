import os
from random import choice
from art import logo, vs
from data import data

score = 0
finished = False

def get_user_answer(user_answer):
  if user_answer == "a":
    return 0
  elif user_answer == "b":
    return 1
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Sorry, that's wrong. Final score: {score}")
    exit()

def get_highest_follower(item1, item2):
  return max(item1["follower_count"], item2["follower_count"])

def get_items():
  item1 = choice(data)
  item2 = choice(data)
  while item1 == item2:
    item2 = choice(data)
  return [item1, item2]

def print_format(item):
    return f"{item['name']}, a {item['description']}, from {item['country']}"

def game():
  global finished, score
  while not finished:
    items = get_items()

    print(logo)
    print(f"Compare A: {print_format(items[0])}")
    print(vs)
    print(f"Against B: {print_format(items[1])}")

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    user_answer = get_user_answer(user_input)
    highest_follower = get_highest_follower(items[0], items[1])

    if items[user_answer]["follower_count"] == highest_follower:
      score += 1
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f"You're right! Current score: {score}")
    else:
      finished = True
      os.system('cls' if os.name == 'nt' else 'clear')
      print(f"Sorry, that's wrong. Final score: {score}")

game()