from turtle import Turtle


FONT = ("Courier", 24, "normal")
WIDTH = 800
HEIGHT = 600


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level = 1
        self.goto(-WIDTH / 2 + 90, HEIGHT / 2 - 50)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game over", align="center", font=("Courier", 24, "bold"))
