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

        self.speed = 3

    def move(self):
        self.fd(self.speed)
        if self.xcor() > 290:
            self.setx(290)
            self.lt(40)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(40)

        if self.ycor() > 290:
            self.sety(290)
            self.lt(40)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(40)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, spriteshap, color, startx, starty):
        Sprite.__init__(self, spriteshap, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(20)

    def turn_right(self):
        self.rt(20)

    def accelerate(self):
        if (self.speed < 10):
            self.speed += 1

    def decelerate(self):
        if (self.speed > -10):
            self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshap, color, startx, starty):
        Sprite.__init__(self, spriteshap, color, startx, starty)
        self.speed = 4
        self.setheading(random.randint(0, 360))

class Ally(Sprite):
    def __init__(self, spriteshap, color, startx, starty):
        Sprite.__init__(self, spriteshap, color, startx, starty)
        self.speed = 4
        self.setheading(random.randint(0, 360))

class Missile(Sprite):
    def __init__(self, spriteshap, color, startx, starty):
        Sprite.__init__(self, spriteshap, color, startx, starty)
        self.shapesize(stretch_wid = 0.3, stretch_len = 0.4, outline = None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"


    def move(self):

        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        if self.xcor() < -290 or self.xcor() > 290 or \
        self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_boarder(self):
        # Boarders
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

# Create Game

game = Game()

game.draw_boarder()




player = Player("triangle", "white", 4, 4)
enemy = Enemy('circle', "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
ally = Ally("square", "blue", 0, 0)

# keyboard bindings

turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

# Main game loop
while True:
    player.move()
    enemy.move()
    missile.move()
    ally.move()

    if player.is_collision(enemy):
        enemy.goto(random.randint(-250, 250), random.randint(-250, 250))

    if missile.is_collision(enemy):
        enemy.goto(random.randint(-250, 250), random.randint(-250, 250))
        missile.status = "ready"
        missile.goto(-1000, 1000)


    if missile.is_collision(ally):
        ally.goto(random.randint(-250, 250), random.randint(-250, 250))
        missile.status = "ready"



delay = input("Enter to finish. ->")




