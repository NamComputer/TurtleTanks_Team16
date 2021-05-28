from tkinter import constants
import turtle
import pygame
from constants import *
from player import Player

from arena import Arena
from score_turtle import ScoreTurtle
from bullet import Bullet
from keyboard import Keyboard

from math import sin, cos, pi

# Create the screen
screen = turtle.Screen()
# Get the canvas
canvas = turtle.getcanvas()
# Create a keyboard
kb = Keyboard(canvas)




# Setup the game!
def setup():
    # Create the window
    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)
        # Hide the default turtle
    turtle.hideturtle()
    # Change the background color
    screen.bgcolor("white")
    # Set the window title
    screen.title("Turtle Tanks")
    # Turn on manuel draw mode for more control
    screen.tracer(False)
    # Remove the window borders
    canvas.config(borderwidth=0, highlightthickness=0)
    
def register_shapes():
    def rotate(point, angle, origin=(0, 0)):
        """
        Rotate a point counterclockwise by a given angle around a given origin.
    
        The angle should be given in radians.
        """
        ox, oy = origin
        px, py = point
        sa, ca = sin(angle), cos(angle)
        dx, dy = px - ox, py - oy
    
        qx = ox + ca * dx - sa * dy
        qy = oy + sa * dx + ca * dy
        return qx, qy
    
    def map_transform(points, angle=pi / 2, dx=0, dy=0, scale=1):
        return list(map(lambda x: rotate((scale * (x[0] + dx), scale * (x[1] + dy)), pi / 2), points))
        
    def build_tank(side, objects):
        tank = turtle.Shape("compound")
        for o in objects:
            tank.addcomponent(*o)
        turtle.addshape("tank_" + side, tank)
    
    # Bullet
    b = turtle.Shape("polygon", ((-5, -5), (-5, 5), (5, 5), (5, -5)))
    turtle.addshape("bullet", b)
    
    circle = screen._shapes["circle"]._data
    
    # 3 wheels
    components = []
    components.append((map_transform(circle, dy=-5), "black"))
    components.append((map_transform(circle, dx=20, dy=-5), "yellow"))
    components.append((map_transform(circle, dx=-20, dy=-5), "black"))
    
    # Tank body
    trapezoid = ((-35, 5), (35, 5), (30, 25), (-30, 25))
    components.append((map_transform(trapezoid), "red"))
    
    # Tank turret / gun
    rectangle = ((30, 15), (30, 20), (60, 20), (60, 15))
    components.append((map_transform(rectangle), "red"))
    build_tank("left", components)
    
    components.pop()
    components.pop()
    components.append((map_transform(trapezoid), "blue"))
    
    rectangle = ((-30, 15), (-30, 20), (-60, 20), (-60, 15))
    components.append((map_transform(rectangle), "blue"))
    
    # Uncomment to draw bounding box for debugging
    #components.append((map_transform(circle, 0, 0, 0, 3), "yellow"))
    build_tank("right", components)

    
    

player_1 = None
player_2 = None
def create_players(game_arena):
    global player_1, player_2
    
    player_1 = Player("p1", (LEFT_EDGE + 100, BOTTOM_EDGE + 100), game_arena, kb)
    kb.register_key("p1", "a", "left")
    kb.register_key("p1", "d", "right")
    kb.register_key("p1", "w", "up")
    kb.register_key("p1", "s", "down")
    kb.register_key("p1", "space", "fire")
    
    player_2 = Player("p2", (RIGHT_EDGE - 100, TOP_EDGE - 100), game_arena, kb)
    kb.register_key("p2", "Left", "left")
    kb.register_key("p2", "Right", "right")
    kb.register_key("p2", "Up", "up")
    kb.register_key("p2", "Down", "down")
    kb.register_key("p2", "Return", "fire")
    

    turtle.listen()


gameover = None
score = ScoreTurtle()


def input():
    window = turtle.Screen()
    # window.setup(500,500)
    name = turtle.textinput("1st","1st tank's name")
    return name

def input_2():
    window = turtle.Screen()
    # window.setup(500,500)
    name_2 = turtle.textinput("2nd","2nd tank's name")
    return name_2


# def pause():
#     paused = True
#     while paused:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             if event.type ==pygame.KEYDOWN:
#                 if event.key == pygame.K_c:
#                     paused = False
#                 elif event.key == pygame.K_q:
#                     pygame.quit()
#                     quit()
#         screen.fill("white")


#is_paused = False
wn = turtle.Screen()
# def pause():
#     global is_paused
#     if is_paused == True:
#         is_paused == False
#     else:
#         is_paused == True 

# wn.listen()
# wn.onkeypress(pause,"p")

score_tanks_P1 = 0
score_tanks_P2 =0 
gameover = False
winner = None

def pause(x,y):
    turtle.setpos(0,0)
    # del(score.game_over())
    turtle.penup()
    turtle.clear()
    gameover ==  False
    winner = None
    score_tanks_P1 = 0
    score_tanks_P2 =0 
    draw()
def start():
    global game_state
    game_state = "game"

wn.listen()
wn.onkeypress(start,"p")


def draw():
    style = ("Arial bold", 15)
    game_state = "test"
    global score_tanks_P1
    global score_tanks_P2
    global gameover,winner
    a = input()
    b = input_2()
    text_p1 = turtle.Turtle()
    text_p2 = turtle.Turtle()
    text_p1.penup()
    text_p2.penup()
    text_p1.setpos(-345,320)
    text_p1.write("Score of "+str(a)+ ": " + str(score_tanks_P1),font=style)
    text_p2.setpos(-345,300)
    text_p2.write("Score of "+str(b)+ ": " +str(score_tanks_P2),font=style)
    turtle.clear()
    
    while gameover is False :
        # if game_state =="test":
        #    wn.bgpic("Home_Pic.gif")
        # elif game_state == "game":
        for entity in screen.turtles():
            if isinstance(entity, Bullet) and entity.alive and entity.update() is None:
                # gameover = False
                # winner = None
                if entity.distance(player_1) <= (player_1.radius + entity.radius) and entity.owner is not "p1":
                    entity.alive = False
                    entity.hideturtle()
                    gameover = player_1.hit()
                    score_tanks_P1 +=1
                    
                    text_p1.clear()  
                    text_p1.setpos(-340,320)
                    text_p1.penup()
                    text_p1.write("Score of "+str(a)+ " " + str(score_tanks_P1),font=style)
                    
                    if gameover :

                        winner = a
                    
                elif entity.distance(player_2) <= (player_2.radius + entity.radius) and entity.owner is not "p2":
                    entity.alive = False
                    entity.hideturtle()
                    gameover = player_2.hit()
                    score_tanks_P2 +=1
                    
                    
                    text_p2.clear()
                    text_p2.penup()
                    text_p2.setpos(-340,300)
                    text_p2.write("Score of "+str(b)+ " " +str(score_tanks_P2),font=style)
                    
                    if gameover:
                        winner = b
                if gameover is True and winner is not None:
                    score.game_over(winner)
                    if turtle.onscreenclick(pause,1) is True:
                    
                        pass
                    if game_state == "game":
                        wn.bgpic("Untitled.png")
                    return   
            
                
        player_1.update()
        player_2.update()

        # Draw the objects on the screen!
        screen.update()
        # Redraw every 20 milliseconds
        #canvas.after(20, draw)
        wn.listen()



setup()
register_shapes()

game_arena = None

import tutorial
game_arena = tutorial.game_arena
if not isinstance(game_arena, Arena):
    raise RuntimeError 

create_players(game_arena)

draw()


# Required for every turtle program
turtle.mainloop()