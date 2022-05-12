import imp
from turtle import Turtle

class Ball(Turtle):

  def __init__(self):
    super().__init__()
    self.create_ball()
    self.x_dir = 10
    self.y_dir = 10


  def create_ball(self):
    self.penup()
    self.shape('square')
    self.color('white')
    self.goto(0, 0)
    self.move_speed = 0.1


  def move(self):
    x = self.xcor() + self.x_dir
    y = self.ycor() + self.y_dir
    self.goto(x,y)


  def bounce_y(self):
    self.y_dir *= -1

  
  def bounce_x(self):
    self.x_dir *= -1

  
  def reset_ball(self):
    self.goto(0, 0)
    self.bounce_x()
    self.move_speed = 0.1


  def increase_speed(self):
    if self.move_speed > 0.02:
      self.move_speed *= 0.8
    else:
      self.move_speed = 0.01