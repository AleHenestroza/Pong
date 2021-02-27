from turtle import Turtle

LINE_LEN = 25
BLANK_LEN = 40
HALF_SCREEN_Y = 500


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pensize(7)
        self.color("white")
        self.draw_dotted_line()

    def draw_dotted_line(self):
        self.goto(x=0, y=-HALF_SCREEN_Y)
        self.setheading(90)
        for x in range(40):
            if x % 2 == 0:
                self.penup()
                self.forward(BLANK_LEN)
            else:
                self.pendown()
                self.forward(LINE_LEN)
