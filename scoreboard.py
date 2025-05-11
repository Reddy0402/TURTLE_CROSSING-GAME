from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.LEVEL =1
        self.hideturtle()
        self.penup()
        self.goto(-280,280)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL:{self.LEVEL}", align="LEFT", font=FONT)
        # self.update_scoreboard()

    def increase(self):
        self.LEVEL +=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="CENTER", font=FONT)