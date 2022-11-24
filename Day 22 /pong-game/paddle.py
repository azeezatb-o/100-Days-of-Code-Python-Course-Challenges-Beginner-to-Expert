from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        # self.paddle = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
