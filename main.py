# El clásico juego de Pong, utilizando la librería de Python Turtle Graphics
# Creado por Alejandro Henestroza
# Todos los componentes de este programa pueden ser copiados, reutilizados y redistribuidos

from turtle import Screen
from ball import Ball
from line import Line
from paddle import Paddle
import time


# Setup de la pantalla
screen = Screen()
screen.setup(width=800, height=600, startx=560, starty=240)
screen.bgcolor("black")
screen.title("Pong - by AleHenestroza")
dotted_line = Line()

# Actualización de pantalla
screen.tracer(0)

# Setup objetos
ball = Ball()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Listeners
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Loop principal
running = True
while running:
    time.sleep(0.075)
    screen.update()
    ball.move()

    # Detección de colisión con las paredes
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


screen.exitonclick()
