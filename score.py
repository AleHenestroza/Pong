from turtle import Turtle


class Score(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=coordinates[0], y=coordinates[1])
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=str(self.score), align="center", font=("Courier", 48, "normal"))

    def add_score(self):
        self.score += 1
        self.write_score()
