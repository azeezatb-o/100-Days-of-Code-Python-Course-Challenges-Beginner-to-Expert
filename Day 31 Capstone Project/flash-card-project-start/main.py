from tkinter import *
import pandas
from random import choice
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
data_dict = []

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    f_data = pandas.read_csv("data/french_words.csv")
    data_dict = f_data.to_dict(orient="records")
else:
    # orient="records" presents the data as a list of dictionaries
    data_dict = data.to_dict(orient="records")


def next_word():
    global current_card
    current_card = choice(data_dict)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(card_bg, image=front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(card_bg, image=back_img)


def known():
    data_dict.remove(current_card)
    words_to_learn = pandas.DataFrame(data_dict)
    # index=False does not add index to the csv file being created
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_word()


# UI SETUP
window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#window.after(3000, func=flip_card)

front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bg = canvas.create_image(400, 263, image=front_img)
title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=next_word)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightbackground=BACKGROUND_COLOR, highlightthickness=0, command=known)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()
