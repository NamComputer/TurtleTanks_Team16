from turtle import Turtle
from bullet import Bullet
from constants import *
import winsound

from math import sin, cos, pi
import time

TWO_PI = 2 * pi
class Player(Turtle):

    def __init__(self, name, coord, game_arena, kb):
        Turtle.__init__(self)
        
        self.speed(0)
        self.penup()
        
        if name is "p1":
            self.shape("tank_left")
            self.mult = 1
        else:
            self.shape("tank_right")
            self.mult = -1
        self.radians()
        self.seth(0)
        
        self.step_size = self.mult * PLAYER_SPEED
        self.turn_size = PLAYER_TURN_SPEED * pi / 180
        self.fireTime = -1
        self.health = PLAYER_HEALTH
        self.radius = 30
        
        self.name = name
        self.setx(coord[0])
        self.sety(coord[1])
        self.kb = kb
        self.obstacles = game_arena.get_obstacles()
        
    def is_inside(self, x, y):
        return (abs(x) + self.radius) < BORDER and (abs(y) + self.radius) < BORDER
    
    def right_turn(self):
        self.seth((self.heading() - self.turn_size) % TWO_PI)
    
    def left_turn(self):
        self.seth((self.heading() + self.turn_size) % TWO_PI)
        
    def forward_move(self):
        angle = self.heading()
        tempx = self.xcor() + self.step_size * cos(angle)
        tempy = self.ycor() + self.step_size * sin(angle)

        if self.is_inside(tempx, tempy):
            for obstacle in self.obstacles:
                if obstacle.collides_with(tempx, tempy, self.radius):
                    return
            self.setx(tempx)
            self.sety(tempy)
            
    def backward_move(self):
        angle = pi + self.heading()
        tempx = self.xcor() + self.step_size * cos(angle)
        tempy = self.ycor() + self.step_size * sin(angle)
        if self.is_inside(tempx, tempy):
            for obstacle in self.obstacles:
                if obstacle.collides_with(tempx, tempy, self.radius):
                    return
            self.setx(tempx)
            self.sety(tempy)
            
    def hit(self):
        print("Hit!")
        winsound.PlaySound('sound/hit.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        a = self.health
        if self.health == 1:
            return True
        else:
            self.health -= 1 
            return False
        return a
    

    def fire(self):
        Bullet(self.xcor(), self.ycor(), self.heading() if self.name is "p1" else self.heading() + pi, self.obstacles, self.name)
            
    def update(self):
        # Handle keyboard input
        if self.kb.is_pressed(self.name, "up"):
            self.forward_move()
        elif self.kb.is_pressed(self.name, "down"):
            self.backward_move()
    
        if self.kb.is_pressed(self.name, "left"):
            self.left_turn()
        elif self.kb.is_pressed(self.name, "right"):
            self.right_turn()

        if self.kb.is_pressed(self.name, "fire"):
            if self.fireTime == -1:
                self.fireTime = time.time()
                self.fire()
            elif self.fireTime != -1:
                dt = time.time() - self.fireTime
                if dt < FIRE_RATE:
                    return
                self.fireTime = time.time()
                self.fire()
    
    