import turtle as t
import random as ra

timmy = t.Turtle()
t.colormode(255)


def random_color():
    r = ra.randint(0, 255)
    g = ra.randint(0, 255)
    b = ra.randint(0, 255)
    rgb = (r, g, b)
    return rgb

rand_move = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(5)

for i in range(100):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(ra.choice(rand_move))


my_screen = t.Screen()
my_screen.exitonclick()