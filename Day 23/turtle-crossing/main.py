import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.generate_car()
    car.move()

    # Detect collision with car
    for c in car.cars:
        if player.distance(c) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Determines if the player crossed the road successfully
    if player.is_at_finish_line():
        player.refresh()
        car.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()
