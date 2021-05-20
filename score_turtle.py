from turtle import Turtle

class ScoreTurtle(Turtle):
    
    def __init__(self):
        Turtle.__init__(self)
        
        self.speed(0)
        self.hideturtle()
        
    def update_score(self, player, score):
        pass
    
    def game_over(self, winner):
        self.color("green")
        self.goto(0, 250)
        self.write("GAME OVER\nWinner: " + winner, font=("Arial bold", 30), align="center")