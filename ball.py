from turtle import Turtle

MOVE_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + MOVE_SPEED
        new_y = self.xcor() + MOVE_SPEED
        self.goto(new_x, new_y)
