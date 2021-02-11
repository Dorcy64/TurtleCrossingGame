import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Car Turtle Game")
screen.tracer(0)
player = Player()
car = CarManager()
time.sleep(0.001)
screen.listen()

score = Scoreboard()


TIMES = 1
LEVEL = 6

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if TIMES % LEVEL == 0:
        car.new_car()
    car.move()

    screen.onkey(key="Up", fun=player.up)
    if player.ycor() >= 280:
        player.goto(0, -280)
        score.level()
        if LEVEL >= 3.5:
            LEVEL += -0.75


    for cars_ in car.new_cars:
        if cars_.distance(player) < 20:
            score.game_over()
            game_is_on = False
    TIMES += 1

screen.exitonclick()
