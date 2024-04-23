import os
import random
import time

# Import the turtle module
import turtle
# Required by MacOSx
turtle.fd(0)
# Animation speed
turtle.speed(0)
# Background color
turtle.bgcolor("Black")

turtle.bgpic("img.png")

# Hide the default turtle
turtle.ht()
# Memory
turtle.setundobuffer(1)
# Speed up drawing
turtle.tracer(0)

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
        if (self.xcor() >= (other.xcor() - 15)) and \
        (self.xcor() <= (other.xcor() + 15)) and \
        (self.ycor() >= (other.ycor() - 15)) and \
        (self.ycor() <= (other.ycor() + 15)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, spriteshap, color, startx, starty):
        Sprite.__init__(self, spriteshap, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 0
        self.lives = 3

    def turn_left(self):
        self.lt(20)

    def turn_right(self):
        self.rt(20)

    def accelerate(self):
        if (self.speed < 20):
            self.speed += 1

    def decelerate(self):
        if (self.speed > -20):
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
        self.shapesize(stretch_wid = 0.1, stretch_len = 0.4, outline = None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            os.system("afplay fire.mp3&")
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
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))


# Create Game

game = Game()

game.draw_boarder()

game.show_status()


player = Player("triangle", "white", 4, 4)
missile = Missile("triangle", "yellow", 0, 0)


enemies = []
for i in range(6):
    enemies.append(Enemy("circle", "red", random.randint(-200, 200), random.randint(-200, 200)))

allies = []
for i in range(6):
    allies.append(Ally("square", "blue", random.randint(-200, 200), random.randint(-200, 200)))


# keyboard bindings

turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

# Main game loop
while True:
    turtle.update()
    time.sleep(0.02)
    player.move()
    missile.move()

    for enemy in enemies:
        enemy.move()

        if player.is_collision(enemy):
            os.system("afplay bad.mp3&")
            enemy.goto(random.randint(-250, 250), random.randint(-250, 250))
            game.score -= 150
            game.show_status()

        if missile.is_collision(enemy):
            os.system("afplay good.mp3&")
            enemy.goto(random.randint(-250, 250), random.randint(-250, 250))
            missile.status = "ready"
            missile.goto(-1000, 1000)
            game.score += 100
            game.show_status()

    for ally in allies:
        ally.move()
        if missile.is_collision(ally):
            os.system("afplay bad.mp3&")
            ally.goto(random.randint(-250, 250), random.randint(-250, 250))
            missile.status = "ready"
            missile.goto(-1000, 1000)
            game.score -= 100
            game.show_status()

delay = input("Enter to finish. ->")




