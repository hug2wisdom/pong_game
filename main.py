from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

PADDLE_LEFT_POSITION = -380
PADDLE_RIGHT_POSITION = 380
SCOREBOARD_LEFT_POSITION = -200
SCOREBOARD_RIGHT_POSITION = 200


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.tracer(0)

ball = Ball()

paddle_left = Paddle(PADDLE_LEFT_POSITION)
paddle_right = Paddle(PADDLE_RIGHT_POSITION)

scoreboard_left = Scoreboard(SCOREBOARD_LEFT_POSITION)
scoreboard_right = Scoreboard(SCOREBOARD_RIGHT_POSITION)


screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    if paddle_left.distance(ball) < 30:
        ball.kick()
        scoreboard_left.increase()
    
    if paddle_right.distance(ball) < 30:
        ball.kick()
        scoreboard_right.increase()


screen.exitonclick()
