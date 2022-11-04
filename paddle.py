from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(coord)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
