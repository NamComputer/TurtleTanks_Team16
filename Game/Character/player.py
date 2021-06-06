from turtle import Turtle
from Game.Character.bullet import Bullet
from Game.Main.constants import *
import winsound

from math import sin, cos, pi
import time
import turtle
TWO_PI = 2 * pi

class Player(Turtle):
    """
    A Class that set rules how the tank can turn right, left, move,...

    Attributes
    --------------
        name:str
            return name of the player tank
        coord:
            return coordinate of player tank
        game_arena:
    Methods:
    ---------------
        is_inside(x,y):
            return the player tank always remains in window screen
        right_turn():
            return turn right:
        left_turn():
            return turn_left:
        forward_move():
            return the tank is move forward
        backward_move():
            return the tank is move back
        hit():
            return hit sound when got hit
        update():
            control how the key is pressed and execute it on definition of function in Handling > is_pressed

    """
    
    def __init__(self, name, coord, game_arena, kb):
        """Take in the parameters, Return initialize value of player"""
        Turtle.__init__(self)
        
        self.speed(0)
        self.penup()
        self.health = 0
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
        if self.health == 0:
            def input_health():
                window = turtle.Screen()
                health = turtle.textinput("Health","Input main health:")
                return int(health)
        self.health = input_health()
        self.radius = 30
        
        self.name = name
        self.setx(coord[0])
        self.sety(coord[1])
        self.kb = kb
        self.obstacles = game_arena.get_obstacles()
        
    def is_inside(self, x, y):
        """Take the (x,y),return the player tank always remains in window screen """
        return (abs(x) + self.radius) < BORDER and (abs(y) + self.radius) < BORDER
    
    def right_turn(self):
        """Return The degree when turn right"""
        self.seth((self.heading() - self.turn_size) % TWO_PI)
    
    def left_turn(self):
        """Return The degree when turn left"""
        self.seth((self.heading() + self.turn_size) % TWO_PI)
        
    def forward_move(self):
        """Take in the key u pressed, Return the tank goes forward"""
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
        """Take in the key u pressed, Return the tank goes backward"""
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
        """Return the sound when bullet hit other tank"""
        print("Hit!")
        winsound.PlaySound('Game\Sounds\sound\hit.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        print(self.health)
        if self.health == 1 :
            return True
        else:
            self.health -= 1 
            return False
    

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
    
    