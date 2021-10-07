import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States Game")
image = "india_map_states.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(height=600)

state = turtle.Turtle()
state.penup()
state.hideturtle()

data = pd.read_csv("india_states.csv")

states = 0
states_guessed = []

while states < 31:
    if states > 0:
        ans = screen.textinput(title=f"{states}/30 States Correct", prompt="What's another state")
    else:
        ans = screen.textinput(title="Guess the State", prompt="What's another state")

    if ans.upper() == "EXIT":
        for s in data['states'].to_list():
            if s not in states_guessed:
                state.goto(int(data.x[data.states == s]),int(data.y[data.states == s]))
                state.color("blue")
                state.write(f"{s}")
        break
    
    if ans.upper() in data['states'].to_list() and ans.upper() not in states_guessed:
        state.goto(int(data.x[data.states == ans.upper()]),int(data.y[data.states == ans.upper()]))
        state.write(f"{ans.upper()}")
        states_guessed.append(ans.upper())
        states += 1
        
    
    
        
    
