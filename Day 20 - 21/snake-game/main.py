from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# Turns off the method responsible for tracing the screen activities since the turtles are not
# moving together when it is on
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

on = True

while on:
    # This is the method that then refreshes the screen and tells the screen to print the turtles at the same time
    # so that they can now move together
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        on = False
        scoreboard.game_over()

    # Detect collision with the tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            on = False
            scoreboard.game_over()

screen.exitonclick()
