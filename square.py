# Jacob Benedek 514-887-2148

#Draw a square

import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    line = turtle.Turtle()
    line.color("blue")
    line.speed(-10)

    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    line.forward(100)
    line.right(90)
    line.forward(100)

    circle = turtle.Turtle()
    circle.shape("arrow")
    circle.color("yellow")
    circle.circle(100)
               
    window.exitonclick()

draw_square()

