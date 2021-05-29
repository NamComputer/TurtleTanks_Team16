from turtle import Turtle
from Game.main.constants import *

from math import sin, cos

class Bullet(Turtle):
    
    def __init__(self, x, y, heading, obstacles, owner):
        Turtle.__init__(self)
        
        self.speed(0)
        self.penup()
        self.shape("bullet")
        self.setx(x)
        self.sety(y)
        self.radians()
        self.seth(heading)
        
        self.step_size = BULLET_SPEED 
        self.radius = 5
        self.obstacles = obstacles
        self.owner = owner
        self.alive = True
        
    def is_inside(self, x, y):
        return (-BORDER < x < BORDER) and (-BORDER < y < BORDER)
        
    def has_collided(self):
        x, y = self.position()
        if self.is_inside(x, y):
            for obstacle in self.obstacles:
                if obstacle.collides_with(x, y, self.radius):
                    return True
            return False
        else:
            return True
        
    def update(self):
        if not self.isvisible() or not self.alive:
            return        
        if not self.has_collided():
            angle = self.heading()
            self.setx(self.xcor() + self.step_size * cos(angle))
            self.sety(self.ycor() + self.step_size * sin(angle))
            return
        else:
            print("Despawning")
            self.hideturtle()
            self.alive = False
            return
