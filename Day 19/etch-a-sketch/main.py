from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(30)
    tim.forward(10)


def counter_clockwise():
    tim.left(30)
    tim.forward(10)


def clear_drawing():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=clockwise)

screen.exitonclick()
