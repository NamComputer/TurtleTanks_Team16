from turtle import Screen, Turtle
import time
import turtle
class ScoreTurtle(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        
        self.speed(0)
        self.hideturtle()
        
    def update_score(self, player, score):
        pass
    
    def game_over(self, winner):
        self.color("green")
        sel.goto(0, 250)
        self.write("GAME OVER\nWinner: " + winner, font=("Arial bold", 25), align="center")
        time.sleep(2.4)
        self.goto(0,0)
        self.write("Click left to play again", font=("Arial bold", 35), align="center")