from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, x_position, y_position = 260):
        super().__init__()
        self.x_position = x_position
        self.y_position = y_position
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(self.x_position, self.y_position)
        self.write(f"SCORE: {self.score}", False, "center", ("Arial", 18, "normal"))

    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"SCORE: {self.score}", False, "center", ("Arial", 18, "normal"))