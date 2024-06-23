letter = ""

def write_letter(name):
  mail = letter.replace("[name]", name)
  with open(f"Output/ReadyToSend/to_{name}.txt", "w") as f:
    f.write(mail)

with open("Input/Letters/starting_letter.txt") as f:
  letter = f.read()

with open("Input/Names/invited_names.txt") as f:
  for name in f.readlines():
    write_letter(name.strip())
