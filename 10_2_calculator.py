print("Welcome to the calculator")

def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def calculate(first_number, second_number, operation):
  operate = operations[operation]
  return operate(first_number, second_number)

finished = False
total = 0
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

total = float(input("Input your number: "))

while not finished:
  operation = input("select operation (+ - / *): ")
  num2 = float(input("Input your number: "))

  total = calculate(total, num2, operation)
    
  is_continue = input("Do you want to continue (y) or sum the equation (n) ? ").lower()
  if is_continue != "y":
    finished = True
    final = "{:.2f}".format(total)
    print(f"The result is: {final}")
