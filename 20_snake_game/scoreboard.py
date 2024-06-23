from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = self.read_high_score()
    self.color("white")
    self.penup()
    self.goto(0, 260)
    self.hideturtle()
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)
  
  def reset(self):
    if self.score > self.high_score:
      self.update_high_score()
    self.score = 0
    self.update_scoreboard()

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", align=ALIGN, font=FONT)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()
  
  def read_high_score(self):
    with open("data.txt") as file:
      return int(file.read())
  
  def update_high_score(self):
    self.high_score = self.score
    with open("data.txt", "w") as file:
      file.write(str(self.score))
