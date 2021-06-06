from turtle import Turtle
from Game.Main.constants import *

from math import sin, cos

class Bullet(Turtle):
    """
    A class to control the distance, and control how the bullet can go and make contact

    Attributes
    ------------
        heading:
        obstacles: list
            a list of obstacle 
        owner: str

    Methods
    ---------------
    is_inside(x,y):
        return that the bullet is inside the window of game
    has_collied():
        return True or False depent on the bullet is collision
    update():
        print "Despawning" when it not hit
    """
    
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
        """Take in x,y, return bullet coor inside window game"""

        return (-BORDER < x < BORDER) and (-BORDER < y < BORDER)
        
    def has_collided(self):
        """Take in postition of bullet, return True or False depent on the bullet is collision with obstacle"""
        x, y = self.position()
        if self.is_inside(x, y):
            for obstacle in self.obstacles:
                if obstacle.collides_with(x, y, self.radius):
                    return True
            return False
        else:
            return True
        
    def update(self):
        """Return "Despawning" when bullet is fire"""
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
