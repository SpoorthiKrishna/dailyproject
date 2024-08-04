from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.move()
    def move(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("arial", 24, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("arial", 24, "normal"))


    def l_board(self):
        self.l_score+=1
        self.move()


    def r_board(self):
        self.r_score+=1
        self.move()