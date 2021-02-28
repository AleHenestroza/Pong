# El clásico juego de Pong, utilizando la librería de Python Turtle Graphics
# Creado por Alejandro Henestroza
# Todos los componentes de este programa pueden ser copiados, reutilizados y redistribuidos

from turtle import Screen
from ball import Ball
from line import Line
from paddle import Paddle
from score import Score
import time

# Máquina de estado para seguir qué teclas son presionadas
keys_pressed = {}


# Callback para el event listener KeyPress. Pone el estado de tecla presionada en True
def pressed(event):
    keys_pressed[event.keysym] = True


# Callback para el event listener KeyRelease. Pone el estado de tecla presionada en False
def released(event):
    keys_pressed[event.keysym] = False


# Setup de los event listeners, usando directamente el Canvas de TKinter, en lugar de la clase Screen de Turtle Graphics
# Esto es necesario para acceder al objeto evento, así la máquina de estado puede determinar qué tecla se presionó
def set_key_binds():
    for key in ["Up", "Down", "w", "s"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


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
l_score = Score((-100, 200))
r_score = Score((100, 200))

# Listeners
screen.listen()
set_key_binds()

# Loop principal
running = True
while running:
    time.sleep(0.01)
    # Revisar estado de teclas presionadas y responder adecuadamente
    if keys_pressed["w"]:
        l_paddle.up()
    if keys_pressed["s"]:
        l_paddle.down()
    if keys_pressed["Up"]:
        r_paddle.up()
    if keys_pressed["Down"]:
        r_paddle.down()
    screen.update()
    ball.move()

    # Detección de colisión con las paredes
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detección de colisión con las paletas
    if (ball.distance(r_paddle) < 55 and ball.xcor() > 330) or (ball.distance(l_paddle) < 55 and ball.xcor() < -330):
        ball.bounce_x()

    # Detección de puntos
    if ball.xcor() > 390:
        ball.reset_position()
        l_score.add_score()

    if ball.xcor() < -390:
        ball.reset_position()
        r_score.add_score()


screen.exitonclick()
