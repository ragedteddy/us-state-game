import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US-state_game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
states = df["state"].tolist()
x_coordinates = df["x"].tolist()
y_coordinates = df["y"].tolist()

tim = turtle.Turtle()
tim.hideturtle()
tim.penup()

guessed = []

while len(guessed) < 50:
    answer = screen.textinput(title="Guess the State", prompt="Enter a State's name").lower()
    for i in range(len(states)):
        if states[i].lower() == answer and i not in guessed:
            tim.goto(x_coordinates[i], y_coordinates[i])
            tim.write(states[i])
            guessed.append(i)


screen.exitonclick()


