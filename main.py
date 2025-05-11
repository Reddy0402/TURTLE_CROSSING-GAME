from turtle import Turtle,Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

player = Player()
turtle = Turtle()
screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

#TURTLE MOVE
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    turtle.speed("slowest")
    car_manager.create_cars()
    CarManager.move_cars(self=car_manager)
    #detect collision
    for car in car_manager.all_cars:
       if  car.distance(player) < 15:
           game_is_on = False
           scoreboard.game_over()


    #detect player reached other side
    if player.o_fin():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase()




screen.exitonclick()