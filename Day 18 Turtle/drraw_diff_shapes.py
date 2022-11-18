from turtle import Turtle, Screen
from random import random

timmy = Turtle()


def make_shape(no_of_sides):
    r = random()
    g = random()
    b = random()

    for x in range(no_of_sides):
        timmy.pencolor(r, g, b)
        timmy.forward(100)
        timmy.right(360 / no_of_sides)


for i in range(3, 11):
    make_shape(i)


my_screen = Screen()
my_screen.exitonclick()