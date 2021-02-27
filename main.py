# El clásico juego de Pong, utilizando la librería de Python Turtle Graphics
# Creado por Alejandro Henestroza
# Todos los componentes de este programa pueden ser copiados, reutilizados y redistribuidos

from turtle import Screen
from ball import Ball
from line import Line


# Screen setup
screen = Screen()
screen.setup(width=800, height=600, startx=560, starty=240)
screen.bgcolor("black")
screen.title("Pong - by AleHenestroza")

dotted_line = Line()

# Setup objetos
ball = Ball()

# Loop principal
running = True
while running:
    ball.move()


screen.exitonclick()
