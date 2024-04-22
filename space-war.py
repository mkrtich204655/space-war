import os
import random

# Import the turtle module
import turtle
# Required by MacOSx
turtle.fd(0)
# Animation speed
turtle.speed(0)
# Background color
turtle.bgcolor("Black")
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

    def move(self):
        self.fd(self.speed)

class Player(Sprite):
    def __init__(self, spriteshap, color, startx, starty):
        Sprite.__init__(self, spriteshap, color, startx, starty)
        self.speed = 1
        self.lives = 4

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1



player = Player("triangle", "white", 5, 5)

# keyboard bindings

turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

# Main game loop
while True:
    player.move()


delay = input("Enter to finish. ->")




