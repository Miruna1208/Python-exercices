from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "pink", "blue", "green"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randrange(1, 6) == 1:
            self.hideturtle()
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_spped(self):
        self.speed += MOVE_INCREMENT

    

