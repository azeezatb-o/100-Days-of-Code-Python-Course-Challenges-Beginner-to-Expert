import turtle as t
import random as ra

tim = t.Turtle()

t.colormode(255)
#tim.speed("fastest")
tim.speed(0)
tim.pensize(2)
tim.hideturtle()


def random_color():
    r = ra.randint(0, 255)
    g = ra.randint(0, 255)
    b = ra.randint(0, 255)
    rgb = (r, g, b)
    return rgb


def draw_spirograph(tilt_size):
    for i in range(int(360 / tilt_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.right(tilt_size)


draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()
