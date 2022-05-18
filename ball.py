from turtle import Turtle
from random import randint, random
START_POSITION = (0, 0)
MOVE_DISTANCE = 10
MOVE_DIRECTION = [-1, 1]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(START_POSITION)
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def kick(self):
        self.x_move *= -1

    def ball_home(self):
        self.goto(START_POSITION)
        self.x_move *= random.choice(MOVE_DIRECTION)
        self.y_move *= random.choice(MOVE_DIRECTION)
