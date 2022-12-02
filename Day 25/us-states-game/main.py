import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess a state in the U.S.").title()
    if answer_state == "Exit":
        for st in states:
            if st not in guessed_states:
                missed_states.append(st)
                df = pandas.DataFrame(missed_states)
                df.to_csv("states_to_learn.csv")
        break
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data["state"] == answer_state]
        t.goto(int(state["x"]), int(state["y"]))
        t.write(arg=answer_state, align="center", font=("Courier", 10, "normal"))


# def get_mouse_click_coor(x. y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

#screen.exitonclick()
