from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAME_OVER_FONT = ("Courier", 40, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=GAME_OVER_FONT, align=ALIGNMENT)
