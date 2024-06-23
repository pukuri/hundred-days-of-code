import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
prompt_letters = int(input("How many letters do you want? "))
prompt_numbers = int(input("How many numbers do you want? "))
prompt_symbols = int(input("How many symbols do you want? "))

password = []
for i in range(0, prompt_letters):
  password.append(random.choice(letters))

for i in range(0, prompt_numbers):
  password.append(str(random.randint(0, 10)))

for i in range(0, prompt_symbols):
  password.append(random.choice(symbols))

result = ''
for i in random.shuffle(password):
  result += i

print(result)
