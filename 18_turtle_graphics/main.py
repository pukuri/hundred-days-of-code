import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.shape("turtle")
# timmy.pensize(10)
timmy.speed("fastest")

# for _ in range(15):
#   timmy.forward(10)
#   timmy.penup()
#   timmy.forward(10)
#   timmy.pendown()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)

def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    timmy.forward(100)
    timmy.right(angle)

# for shape_side_n in range(3, 11):
#   timmy.color(random.choice(colors))
#   draw_shape(shape_side_n)

# for _ in range(200):
#   timmy.color(random_color())
#   timmy.forward(30)
#   timmy.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
  for _ in range(int(360 / size_of_gap)):
    timmy.color(random_color())
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading + size_of_gap)

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()