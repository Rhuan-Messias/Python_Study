import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = []
score = Scoreboard()


screen.onkey(player.move, 'w')

game_is_on = True
bias = 5
while game_is_on:
    bias += 1
    if bias == 6:
        cars.append(CarManager())
        bias = 0
    for car in cars:
        car.car_movement()
        if car.distance(player) < 20:
            game_is_on = False 
        elif player.ycor() > 300:
            score.score_increase()
            player.next_level()
            car.next_level_speed()

    time.sleep(0.1)
    screen.update()
