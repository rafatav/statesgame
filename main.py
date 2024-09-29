import turtle
import pandas

guess_states = []

screen = turtle.Screen()
screen.setup(725, 491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

while len(guess_states) < 50:
    state = turtle.Turtle()
    state.penup()
    state.hideturtle()
    state_answer = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state name?").title()

    if state_answer == "Exit":
        break
    for st in range(len(data.state)):
        if data.state[st] == state_answer:
            guess = data[data.state == state_answer]
            x = guess.x.item()
            y = guess.y.item()
            state.goto(x, y)
            state.write(arg=state_answer)
            guess_states.append(state_answer)

for state in guess_states:
    if state in all_states:
        all_states.remove(state)

with open("states_to_learn.csv", mode="w") as states_to_learn:
    for missing_state in all_states:
        missing_state = missing_state + "\n"
        states_to_learn.write(missing_state)
