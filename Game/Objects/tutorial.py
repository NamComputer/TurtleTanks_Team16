from turtle import radians
from Game.Objects.arena import Arena
from Game.main.obstacle import Obstacle
import random
global game_arena

game_arena = Arena()

# ------------------------------------------------------------------------------------
# Add your obstacles here!
# Order: name, list of coords, color, and radius/length & width

x_circle = random.randint(20,100)
y_circle = random.randint(-150,100)
green_circle = Obstacle("circle", [x_circle, y_circle], "green", 60)
game_arena.add_obstacle(green_circle)

x_square = random.randint(-200, 180)
y_square = random.randint(-100,200)
green_square = Obstacle("square", [x_square, y_square], "green", 60)
game_arena.add_obstacle(green_square)

red_rectangle = Obstacle("rectangle", [0, -200], "red", 60, 100)
game_arena.add_obstacle(red_rectangle)

red_rectangle = Obstacle("rectangle", [0, 200], "orange", 60, 100)
game_arena.add_obstacle(red_rectangle)

game_arena.draw_arena()