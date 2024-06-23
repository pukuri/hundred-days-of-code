import random

number = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty == 'easy':
    return 10
  elif difficulty == 'hard':
    return 5
  else:
    return 1

def print_prediction(guess):
  if guess > number:
    print("Too high.")
  else:
    print("Too low.")

attempts = set_difficulty()
correct = False
effort = 0

while not correct:
  if attempts == effort:
    print(f"You lose, the number is {number}.")
    break

  print(f"You have {attempts} attempts remaining to guess the number.")
  effort += 1
  guess = int(input("Make a guess: "))

  if guess != number:
    print_prediction(guess)
    print("Guess again.")
  else:
    correct = True
    print("Correct!")