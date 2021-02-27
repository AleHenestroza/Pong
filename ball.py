from turtle import Turtle
import random

MOVE_SPEED = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.set_random_heading()

    def set_random_heading(self):
        self.setheading(random.randint(0, 359))

    def move(self):
        self.forward(MOVE_SPEED)
