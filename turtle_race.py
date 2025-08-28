from turtle import Turtle, Screen
import random
    
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []
colors = ["red", "orange", "yellow", "pink", "blue", "green"]
forward_move = [0, 1, 2, 3, 4, 5]

for i in range(6):
    tim = Turtle()
    turtles.append(tim)

index = 0
x_pos= -230
y_pos = 90

for tim in turtles:
    tim.penup()
    tim.shape("turtle")
    tim.color(colors[index])
    index += 1
    tim.goto(x_pos, y_pos)
    y_pos -= 30

not_end = True

while(not_end):
    for tim in turtles:
        tim.forward(random.choice(forward_move))
        if tim.xcor() >= 230:
            not_end = False
            winner = tim.pencolor()

if winner == bet:
    print("You won! Winner turtle: " + winner )
else: 
    print("You lost! Winner turtle: " + winner)

screen.exitonclick()