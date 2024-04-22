import os
import random

# Import the turtle module
import turtle
# Required by MacOSx
turtle.fd(0)
# Animation speed
turtle.speed(0)
# Background color
turtle.bgcolor("Red")
# Hide the default turtle
turtle.ht()
# Memory
turtle.setundobuffer(1)
# Speed up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshap, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshap)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)

        self.speed = 1

player = Sprite("triangle", "white", 5, 5)

delay = input("Enter to finish. ->")




