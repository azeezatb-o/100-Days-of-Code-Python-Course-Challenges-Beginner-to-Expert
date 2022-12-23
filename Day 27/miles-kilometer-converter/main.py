from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Labels

label1 = Label(text="Miles")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
label3.grid(row=1, column=1)

label4 = Label(text="Km")
label4.grid(row=1, column=2)


# Entries
entry = Entry(width=5)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

def button_clicked():
    new_text = round(float(entry.get()) * 1.609, 2)
    label3.config(text=f"{new_text}")


#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()