import random

computer_choice = random.randint(0, 2)
your_choice = int(input("Choose: 0 is rock, 1 is paper, 2 is scissors :"))
choices = ["rock", "paper", "scissors"]
outputs = ["You win!", "Computer wins!", "It's a draw!"]

if your_choice > 2 or your_choice < 0:
  print("Wrong choice")
else:
  print(f"You chose {choices[your_choice]}")
  print(f"Computer chose {choices[computer_choice]}")

  if computer_choice == your_choice:
    print(outputs[2])
  elif computer_choice == 0 and your_choice == 2:
    print(outputs[1])
  elif your_choice == 0 and computer_choice == 2:
    print(outputs[0])
  elif computer_choice > your_choice:
    print(outputs[1])
  else:
    print(outputs[0])