from tkinter import *
from tkinter import messagebox
import random
import pyperclip  # A package for copying something to your clipboard for use somewhere else
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for l in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for s in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    # Copies the password generated to user's clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = web_entry.get()
    email = email_entry.get()
    passwd = pass_entry.get()
    pass_data = {
        website: {
            "email": email,
            "password": passwd
        }
    }

    if len(website) == 0 or len(passwd) == 0:
        messagebox.showinfo(title="Oops!", message="Fields cannot be empty! Insert values in each field")
    else:
        try:
            with open("password_data.json", "r") as data:
                # Retrieves json data
                d = json.load(data)
        except FileNotFoundError:
            with open("password_data.json", "w") as data:
                # Save the updated data back in the file
                # indent rearranges the json data in a more readable form other than the single line form,
                # which is the default
                json.dump(pass_data, data, indent=4)
        else:
            # Updates json data with more data
            d.update(pass_data)
            with open("password_data.json", "w") as data:
                # Save the updated data back in the file
                # indent rearranges the json data in a more readable form other than the single line form,
                # which is the default
                json.dump(d, data, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web_data = web_entry.get()
    try:
        with open("password_data.json", "r") as data:
            # Retrieves json data
            d = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if web_data in d:
            messagebox.showinfo(title=web_data, message=f"Email: {d[web_data]['email']} \n"
                                                        f"Password: {d[web_data]['password']}")
        else:
            messagebox.showinfo(title="Warning", message=f"No data for {web_data} exists in the file")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Generator")
window.config(padx=50, pady=50)


logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

# Entries
web_entry = Entry(width=22)
web_entry.grid(row=1, column=1)
web_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "azeezat.b@gmail.com")

pass_entry = Entry(width=22)
pass_entry.grid(row=3, column=1)


# Buttons
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", width=11, command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()