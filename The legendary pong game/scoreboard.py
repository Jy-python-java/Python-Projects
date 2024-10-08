from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align = "center", font=("Courier", 70 , "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    def write_score(self) :
            self.clear()
            self.goto(-100, 200)
            self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
            self.goto(100, 200)
            self.write(self.r_score, align="center", font=("Courier", 70, "normal"))
