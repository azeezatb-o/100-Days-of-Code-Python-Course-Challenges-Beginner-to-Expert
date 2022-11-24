from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Andale Mono", 70, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(50, 230)
        self.write(arg=self.r_score, font=FONT, align=ALIGNMENT)
        self.goto(-50, 230)
        self.write(arg=self.l_score, font=FONT, align=ALIGNMENT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
