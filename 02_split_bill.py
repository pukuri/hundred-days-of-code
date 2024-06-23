print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip_correct = False

while not tip_correct:
  tip = int(input("What percentage tip would you like to give? 10 12 or 15?"))
  if tip == 10 or tip == 12 or tip == 15 :
    tip_correct = True
  else:
    print("False tip")
people = int(input("How many people to split the bill? "))

result = ((bill * (tip / 100)) + bill) / people
final = "{:.2f}".format(result)
print(f"Each person should pay ${final}")


