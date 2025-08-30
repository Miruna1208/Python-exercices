import pandas
import turtle 

data = pandas.read_csv("C:/Users/mirun/Documents/Learning/Python-exercices/Countries_game/50_states.csv")
states = data.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.setup(width=700, height=500)
screen.title("U.S Game")
image = "C:/Users/mirun/Documents/Learning/Python-exercices/Countries_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

countries_guessed = 50
while len(guessed_states) < 50:
    answer = screen.textinput(title="U.S states", prompt=f"Total to guess: {countries_guessed} ").title()
    if answer in states:
        guessed_states.append(answer)
        write_state = turtle.Turtle()
        write_state.penup()
        write_state.hideturtle()
        state_data = data[data.state == answer] 
        write_state.goto(state_data.x.item(), state_data.y.item())   
        write_state.write(answer)   
        countries_guessed -= 1

screen.exitonclick()