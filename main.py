# El clásico juego de Pong, utilizando la librería de Python Turtle Graphics
# Creado por Alejandro Henestroza
# Todos los componentes de este programa pueden ser copiados, reutilizados y redistribuidos

from turtle import Screen, Turtle
from ball import Ball
from line import Line


# Screen setup
screen = Screen()
screen.setup(width=1000, height=800, startx=460, starty=140)
screen.bgcolor("black")
screen.title("The Pong Game - by AleHenestroza")

dotted_line = Line()

# Setup objetos
ball = Ball()

# Loop principal
running = True
while running:
    ball.move()


screen.exitonclick()
