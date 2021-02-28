from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_SPEED = 20


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=1)  # Inicial: 20x20 - Stretched: 100x20
        self.goto(x=coordinates[0], y=coordinates[1])

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)
