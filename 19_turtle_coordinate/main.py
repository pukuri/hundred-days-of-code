import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []

for i in range(0, 6):
  tim = t.Turtle(shape="turtle")
  tim.color(colors[i])
  tim.penup()
  tim.goto(x=-230, y=y_pos[i])
  turtles.append(tim)

if bet:
  race_on = True

while race_on:
  for turtle in turtles:
    if turtle.xcor() > 230:
      race_on = False
      winner = turtle.pencolor()
      if winner == bet:
        print("anda menang")
      else:
        print(f"anda kalah, {winner} is the winner")
    rand_distnc = random.randint(0, 10)
    turtle.forward(rand_distnc)

# def move_forwards():
#   tim.forward(10)

# def move_backwards():
#   tim.backward(10)

# def turn_left():
#   tim.setheading(tim.heading() + 10)

# def turn_right():
#   tim.setheading(tim.heading() - 10)

# def clear():
#   tim.clear()
#   tim.penup()
#   tim.home()
#   tim.pendown()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")



screen.exitonclick()