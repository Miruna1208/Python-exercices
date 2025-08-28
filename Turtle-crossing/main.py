from turtle import Screen, Turtle
from turtle_cross import Turtle_cross
from car import Car
import time
from score import Score

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

tim = Turtle_cross()
screen.onkey(key="Up", fun=tim.move)

car = Car()
car.hideturtle()
score = Score()

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    for item in car.all_cars:
        if item.distance(tim) < 20:
            score.game_over()
            game_on = False

    if tim.finish():
        tim.go_to_start()
        score.increase_level()
        car.increase_spped()



screen.exitonclick()