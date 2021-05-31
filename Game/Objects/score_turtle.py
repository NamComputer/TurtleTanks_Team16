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
    
    def game_over(self, winner,score_tanks):
        self.color("red")
        self.goto(0, 250)
        self.write("GAME OVER\nWinner: " + winner , font=("Arial bold", 25), align="center")
        
        self.goto(0, 220)
        self.write("Score: "+  str(score_tanks) , font=("Arial bold", 25), align="center")
        
        time.sleep(2.4)
        self.goto(0,0)
        self.color("black")
        self.write("Press 'r' to play again\nClick 'right' to exit", font=("Arial bold", 35), align="center")