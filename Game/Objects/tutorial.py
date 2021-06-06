from turtle import radians
from Game.Objects.arena import Arena
from Game.Main.obstacle import Obstacle
import random
global game_arena

def arena():
    game_arena = Arena()

    '''
    Take Obstacle Order: name, list of coords, color, and radius/length & width to create obstacle

                
        Parameters:

        Return: 
            game_arena to build obstacle 
    '''
    
    x_circle = random.randint(-300,300)
    y_circle = random.randint(-300,300)
    green_circle = Obstacle("circle", [x_circle, y_circle], "green", 60)
    game_arena.add_obstacle(green_circle)

    green_square = Obstacle("square", [-200, 200], "green", 60)
    game_arena.add_obstacle(green_square)

    x_rect = random.randint(-300,300)
    y_rect = random.randint(-300,300)
    red_rectangle = Obstacle("rectangle", [x_rect, y_rect], "red", 60, 100)
    game_arena.add_obstacle(red_rectangle)

    red_rectangle = Obstacle("rectangle", [0, 200], "orange", 60, 100)
    game_arena.add_obstacle(red_rectangle)

    game_arena.draw_arena()

    return game_arena