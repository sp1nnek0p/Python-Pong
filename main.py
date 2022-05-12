from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

is_game_running = True

# Create the Screen Object
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Python Pong')
screen.tracer(0)

# Create the White Strip in the middle of the board
board = Turtle()
board.hideturtle()
board.goto(0, 300)
board.setheading(270)
board.color('white')
board.shape('square')
board.shapesize(stretch_wid=0.5, stretch_len=2, outline=None)
board.penup()

for _ in range(7):
  board.stamp()
  board.forward(100)

# Instantiate the Paddle and Score objects
paddle1 = Paddle(player_number=1)
paddle2 = Paddle(player_number=2)
score_player1 = Score(player_number=1)
score_player2 = Score(player_number=2)

# Instantiate the Ball object
ball = Ball()

# Event Listeners for both Paddles
screen.listen()
screen.onkeypress(paddle2.move_up, 'Up')
screen.onkeypress(paddle2.move_down, 'Down')
screen.onkeypress(paddle1.move_up, 'w')
screen.onkeypress(paddle1.move_down, 's')

# Main Game Loop
while is_game_running:
  screen.update()
  # Ball start moving
  ball.move()
  time.sleep(ball.move_speed)

  # Collision with the walls
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Check Collision with the paccles
  # Seperate If statements to keep to PEP readability Standards
  if ball.xcor() > 320 and ball.distance(paddle2) < 60:
    ball.bounce_x()
    ball.increase_speed()

  if ball.xcor() < -320 and ball.distance(paddle1) < 60:
    ball.bounce_x()
    ball.increase_speed()

  # Check if the ball went out of either side of the screen
  # Once again seperate if statements but this time to increment
  # different players scores
  if ball.xcor() > 360:
    ball.reset_ball()
    score_player1.add_to_score()

  if ball.xcor() < -360:
    ball.reset_ball()
    score_player2.add_to_score()



screen.exitonclick()
