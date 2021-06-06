from turtle import Screen, Turtle
import time

class ScoreTurtle(Turtle):

    """
    A Class to show up the score, who win this game

    Attributes
    -------------

    Method
    -------------
    update_score(player,score):
        pass
    gameover(winner,score_tanks):
        Return the notification when the game ended, and the score winner got
    """
    
    # def __init__(self):
    #     '''
        
    #     '''
    #     Turtle.__init__(self)
        
    #     self.speed(0)
    #     self.hideturtle()
        
    # def update_score(self, player, score):
    #     pass
    
    def game_over(self, winner,score_tanks):
        """ Take in winner, score_tanks, return who is the winner, score and show up the option for people to play again or not"""
        
        self.color("red")
        self.goto(0, 250)
        self.write("GAME OVER\nWinner: " + winner , font=("Arial bold", 25), align="center")
        
        self.goto(0, 220)
        self.write("Score: "+  str(score_tanks) , font=("Arial bold", 25), align="center")
        
        time.sleep(2.4)
        self.goto(0,0)
        self.color("black")
        self.write("Press 'r' to play again\nClick 'right' to exit", font=("Arial bold", 35), align="center")