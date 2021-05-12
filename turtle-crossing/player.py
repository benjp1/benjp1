from turtle import Turtle
MOVE_DISTANCE = 10
WIDTH = 800
HEIGHT = 600
STARTING_POSITION = (0, -HEIGHT / 2 + 15)
FINISH_LINE = HEIGHT / 2 - 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.shapesize(0.8, 0.8)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(10)

    def reset_position(self):
        self.goto(STARTING_POSITION)