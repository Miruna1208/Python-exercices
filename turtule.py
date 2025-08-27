from turtle import Turtle, Screen
import random
import turtle
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.color("pink", "blue")
#colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta", "lime", "gold", "turquoise", "violet", "tomato", "salmon", "hotpink", "deepskyblue", "springgreen", "orangered", "chartreuse", "dodgerblue", "mediumvioletred", "lawngreen", "crimson", "aqua"]
direction = [0, 90, 180, 270]
colors = colorgram.extract('C:/Users/mirun/Documents/Learning/Python-exercices/images/OIP.jpg', 30)
turtle.colormode(255)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_random_color = (r, g, b)
    rgb_colors.append(new_random_color)

print(rgb_colors)

#for i in range(6):
#    for i in range(5):
#        timmy.pendown()
#        timmy.forward(10)
#        timmy.penup()
#        timmy.forward(10)
#    timmy.left(60)


def draw_shape(sides):
    angle = 360 / sides
    for i in range(sides):
        timmy.forward(100)
        timmy.left(angle)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)

def move_random_color():
    for i in range(100):
        timmy.forward(30)
        timmy.left(random.choice(direction))
        timmy.pencolor(random_color())

def spirograph():
    for i in range(100):
        timmy.speed("fastest")
        timmy.circle(100)
        timmy.left(5)
        timmy.pencolor(random_color())

def move_random_color_image():
    for i in range(100):
        timmy.forward(30)
        timmy.left(random.choice(direction))
        timmy.pencolor(random.choice(colors))

def dot_pic(list):
    timmy.speed("fastest")
    timmy.penup()
    timmy.setheading(180)
    timmy.forward(300)
    timmy.setheading(270)
    timmy.forward(260)
    timmy.setheading(360)
    for i in range(7):
        for i in range(10):
            timmy.dot(20, random.choice(list))
            timmy.forward(60)
        timmy.dot(20, random.choice(list))
        timmy.left(90)
        timmy.forward(40)
        timmy.left(90)
        for i in range(10):
            timmy.dot(20, random.choice(list))
            timmy.forward(60)
        timmy.dot(20, random.choice(list))
        timmy.right(90)
        timmy.forward(40)
        timmy.right(90)

dot_pic(rgb_colors)
screen = Screen()
screen.exitonclick()