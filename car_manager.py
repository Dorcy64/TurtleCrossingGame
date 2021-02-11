from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def rand_color():
    rand_position = randint(0, (len(COLORS) - 1))
    return COLORS[rand_position]


def random_y():
    rand_y = randint(-250, 280)
    return rand_y


class CarManager:
    def __init__(self):
        self.new_cars = []

    def new_car(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.penup()
        car.speed("slowest")
        car.color(rand_color())
        car.goto(280, random_y())
        self.new_cars.append(car)

    def move(self):
        for car in self.new_cars:
            car.backward(MOVE_INCREMENT)
