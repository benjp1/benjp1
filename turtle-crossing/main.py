import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import random as ran


WIDTH = 800
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = []

screen.listen()
screen.onkey(player.move, "w")
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    if ran.randint(0, 100) > 97:
        cars.append(Car())
    for car in cars:
        car.move()
        if car.squares[-1].xcor() < -WIDTH / 2 - 20:
            cars.remove(car)
            car.clear()
    if player.ycor() > HEIGHT / 2 - 25:
        score.level_up()
        for car in cars:
            car.leveled_up()
        player.reset_position()
    for car in cars:
        for square in car.squares:
            if player.distance(square) < 10:
                game_is_on = False
                score.game_over()

screen.exitonclick()
