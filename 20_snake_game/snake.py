from turtle import Turtle

START_POST = [(-11,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for pos in START_POST:
      self.add_seg(pos)

  def add_seg(self, pos):
    new_seg = Turtle("square")
    new_seg.color("white")
    new_seg.penup()
    new_seg.goto(pos)
    self.segments.append(new_seg)
  
  def reset(self):
    for seg in self.segments:
        seg.goto(1000,1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]

  def extend(self):
    self.add_seg(self.segments[-1].position())

  def move(self):
    for seg in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[seg - 1].xcor()
      new_y = self.segments[seg - 1].ycor()
      self.segments[seg].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)