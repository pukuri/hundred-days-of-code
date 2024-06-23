import random

from art import logo

cards = {
    "Ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10
}
your_cards = []
enemy_cards = []

def add_card(deck, times):
  for i in range(times):
    card = random.choice(list(cards.keys()))
    deck.append(card)

def get_values(deck):
  values = 0
  for i in deck:
    values += cards[i]
  if "Ace" in deck and values > 21:
    values -= 10
  return values

def is_over(deck):
  return get_values(deck) > 21

def determine_winner():
  if is_over(your_cards) and is_over(enemy_cards):
    print("It's a draw!")
  elif is_over(enemy_cards):
    print("The enemy went over. You win!")
  elif is_over(your_cards):
    print("You went over. You lose!")
  elif get_values(your_cards) == get_values(enemy_cards):
    print("It's a draw!")
  elif get_values(your_cards) > get_values(enemy_cards):
    print("You had more score. You win!")
  elif get_values(your_cards) < get_values(enemy_cards):
    print("The enemy had more score. You lose!")

def print_recent_hand():
  print(f"Your hand: {your_cards}, current score: {get_values(your_cards)}")
  print(f"Computer first card: {enemy_cards[0]}")

def print_final_hand():
  print(f"Your final hand: {your_cards}, final score: {get_values(your_cards)}")
  print(f"The enemy final hand: {enemy_cards}, final score: {get_values(enemy_cards)}")
  determine_winner()

def play():
  add_card(your_cards, 2)
  add_card(enemy_cards, 2)

  print(logo)
  print_recent_hand()

  if(get_values(your_cards) == 21):
    print("You got blackjack. You win!")
    return

  if(get_values(enemy_cards) == 21):
    print("You got blackjack. You win!")
    return

  continue_play = input("type 'y' to get another card, type 'n' to pass: ") == "y"

  while continue_play:
    add_card(your_cards, 1)
    if get_values(enemy_cards) < 19:
      add_card(enemy_cards, 1)

    if is_over(your_cards) or is_over(enemy_cards):
      continue_play = False
    else:
      print_recent_hand()
      continue_play = input("type 'y' to get another card, type 'n' to pass: ") == "y"

  print_final_hand()

play()