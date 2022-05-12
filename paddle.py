from turtle import Turtle

class Paddle(Turtle):
  """
  When initiating the Paddle Class player_number should be either 1 or 2
  """
  def __init__(self, player_number):
    super().__init__()
    self.player_number = player_number
    self.create_paddle()

  def create_paddle(self):
    self.penup()
    self.shape('square')
    self.color('white')
    self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
    if self.player_number == 1:
      self.setpos(-350, 0)
    elif self.player_number == 2:
      self.setpos(350, 0)

  def move_up(self):
    new_y = self.ycor() + 20
    self.goto(x=self.xcor(), y=new_y)

  def move_down(self):
    new_y = self.ycor() - 20
    self.goto(x=self.xcor(), y=new_y)