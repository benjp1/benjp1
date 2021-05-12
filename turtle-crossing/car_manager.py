from turtle import Turtle
import random as ran


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
WIDTH = 800
HEIGHT = 600


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 1
        self.squares = []
        self.color = ran.choice(COLORS)
        self.make_car()
        self.hideturtle()

    def make_car(self):
        y = ran.choice(range(int(-HEIGHT / 2 + 40), int(HEIGHT / 2 - 40) + 1, 20))
        for step in range(0, 41, 20):
            square = Turtle()
            square.color(self.color)
            square.penup()
            square.speed(0)
            square.setheading(180)
            square.shape("square")
            square.shapesize(1, 1)
            square.goto(WIDTH / 2 + step, y)
            self.squares.append(square)

    def move(self):
        for square in self.squares:
            square.forward(self.move_speed)

    def leveled_up(self):
        self.move_speed += 0.1
