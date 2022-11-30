from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = 5

    def generate_car(self):
        # Generate a new car only every 6th time the game loop runs
        chance = random.randint(1, 6)
        if chance == 1:
            y = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
