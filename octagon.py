# Jacob Benedek 514-887-2148

#Draw a square

import turtle

window = turtle.Screen()
window.bgcolor("red")

line = turtle.Turtle()

def draw_angle():
    
    line.forward(100)
    line.right(45)
    line.forward(100)
    
x=0
while (x<8):
    draw_angle()
    x=x+1

window.exitonclick()
