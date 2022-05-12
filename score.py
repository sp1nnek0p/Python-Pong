from turtle import Turtle

class Score(Turtle):

  def __init__(self, player_number):
      """
      When initiating the Score Class player_number should be either 1 or 2
      """
      super().__init__()
      self.score = 0
      self.player_number = player_number
      self.create_score()

  def create_score(self):
    self.penup()
    self.hideturtle()
    self.color('white')
    if self.player_number == 1:
      self.goto(-100, 220)
    elif self.player_number == 2:
      self.goto(100, 220)
    self.update_score()    

  def add_to_score(self):
    self.score += 1
    self.update_score()

  def update_score(self):
    self.clear()
    self.write(f'{self.score}', align='center', font=('OCR A Extended', 46, 'bold'))