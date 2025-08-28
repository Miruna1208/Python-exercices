from turtle import Turtle

START_POSITION = (0, -280)
MOVE_FORWARD = 10
FINISH_LINE = 280

class Turtle_cross(Turtle):
    
    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        self.shape("turtle")
        self.penup()
        self.goto(START_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_FORWARD)

    def finish(self):
        if self.ycor() == FINISH_LINE:
            return True
        else: return False

    def go_to_start(self):
        self.clear()
        self.goto(START_POSITION)
