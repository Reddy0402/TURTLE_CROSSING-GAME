import time
from turtle import Turtle


STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.go_to_start()


    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        time.sleep(0.1)
        self.goto(STARTING_POSITION[0],FINISH_LINE_Y)

    def o_fin(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False