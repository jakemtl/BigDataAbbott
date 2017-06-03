# Jacob Benedek 514-887-2148

#Draw a square

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    line = turtle.Turtle()
    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    line.forward(100)

    window.exitonclick()

draw_square()

