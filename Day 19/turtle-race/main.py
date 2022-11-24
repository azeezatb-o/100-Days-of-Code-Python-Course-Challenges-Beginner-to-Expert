from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=500)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

color = ["red", "purple", "yellow", "orange", "blue", "green"]
y_axis = [60, 30, 0, -30, -60, -90]
turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_axis[i])
    turtles.append(new_turtle)


if user_choice:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)


screen.exitonclick()
