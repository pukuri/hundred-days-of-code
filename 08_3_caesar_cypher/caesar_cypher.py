import os

from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
finished = False

def process(text, shift, direction):
  result = ""

  if shift > 26:
    shift = shift % 26

  for i in text:
    if not i.isalpha():
      result += i
    else:
      pos = alphabet.index(i)

      if direction == "encode":
        pos_shifted = pos + shift
      elif direction == "decode":
        pos_shifted = pos - shift
      result += alphabet[pos_shifted]

  print(f"Decoded text is: {result}")

while not finished:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  if (direction == 'encode' or direction == 'decode'):
    process(text=text, shift=shift, direction=direction)
  else:
    print("Wrong input")

  again = input("Want to try again? (y/n)").lower()
  if not again == "y":
    print("Thank you")
    finished = True