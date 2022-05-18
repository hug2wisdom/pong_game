from calendar import TUESDAY
from turtle import Turtle
MOVE_DISTANCE = 40


class Paddle(Turtle):
    def __init__(self, x_position, y_position=0):
        self.x_position = x_position
        self.y_position = y_position
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.x_position, self.y_position)

    def up(self):
        self.goto(self.x_position, self.ycor() + MOVE_DISTANCE)

    def down(self):
        self.goto(self.x_position, self.ycor() - MOVE_DISTANCE)
