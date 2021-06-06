from turtle import Turtle
from Game.Main.constants import *

class Builder(Turtle):
    """

    A Class to build apppearance of the window screen and obstacle on the screen

    Attribute
    -----------
    Method
        draw_arena_outlines():
            draw the outline of window game screen
        draw_shape(obstacle):
            return the shape is drawn 
    """

    
    def __init__(self):
        Turtle.__init__(self)
        
        # Make the builder turtle super fast!
        self.speed(0)
        
    def draw_arena_outline(self):
        # Don't draw when moving!
        self.penup()
        # Teleport the builder to this position
        self.goto(LEFT_EDGE, TOP_EDGE)
        # Start drawing the lines!
        self.pendown()
        # Change the thickness of the line
        self.pensize(5)
        # Set the color of the line
        self.color("green")
        # Four sides of a square
        for count in range(4):
            # Move forward
            self.forward(WINDOW_SIZE - 7)
            # Turn right
            self.right(90)

        # Hide the builder turtle
        self.hideturtle()
        
    def draw_shape(self, obstacle):
        """Take in the name of obstacle, return the shape which is drawn on screen"""
        self.color(obstacle.color)
        if obstacle.shape_name is "circle":
            self.penup()
            self.goto(obstacle.x, obstacle.y - obstacle.radius)
            self.pendown()
            self.begin_fill()
            self.circle(obstacle.radius)
            self.end_fill()
        elif obstacle.shape_name is "square" or obstacle.shape_name is "rectangle":
            self.penup()
            self.goto(obstacle.x - obstacle.length / 2, obstacle.y + obstacle.width / 2)
            self.pendown()
            self.begin_fill()
            for count in range(2):
                self.forward(obstacle.length)
                self.right(90)
                self.forward(obstacle.width)
                self.right(90)
            self.end_fill()