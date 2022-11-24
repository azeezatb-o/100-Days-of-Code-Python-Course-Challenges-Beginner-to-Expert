from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        # self.y_move *= -1 reverses the value of the ycor() in the move() so that the ball moves in reverse direction
        self.y_move *= -1

    def bounce_x(self):
        # self.x_move *= -1 reverses the value of the xcor() in the move() so that the ball moves in reverse direction
        self.x_move *= -1
        self.ball_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

