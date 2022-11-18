from turtle import Turtle, Screen

timmy = Turtle()

for i in range(20):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()
    
my_screen = Screen()

my_screen.exitonclick()
