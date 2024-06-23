import random
import os

from hangman_words import word_list
answer = []
end_game = False
lives = 6

#PRINT LOGO
from hangman_art import logo
print(logo)

chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}")
for i in chosen_word:
	answer.append("_")

print(f"{' '.join(answer)}")
while not end_game:
	correct = False
	letter = input("Put your letter: ").lower()
	os.system('cls' if os.name == 'nt' else 'clear')

	for index, i in enumerate(chosen_word):
		if i == letter:
			answer[index] = letter
			correct = True

	if correct:
		print(f"{' '.join(answer)}")
	else:
		lives -= 1
		print(f"{' '.join(answer)}")
		from hangman_art import stages
		print(stages[lives])


	if "_" not in answer:
		end_game = True
		print("You won")
	elif lives <= 0:
		end_game = True
		print("You lose")