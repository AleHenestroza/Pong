from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_SPEED = 20


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=1)
        self.goto(x=coordinates[0], y=coordinates[1])

    def up(self):
        new_y = self.ycor() + PADDLE_SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_SPEED
        self.goto(self.xcor(), new_y)