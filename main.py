from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=500, height=300)


def calculate():
    num = float(my_input.get())
    num *= 1.6
    my_label2.config(text=num)


my_input = Entry()
my_input.config(width=5)
my_input.insert(END, string="0")
my_input.grid(column=1, row=1)

my_label1 = Label(text="Miles")
my_label1.grid(column=2, row=1)

my_label2 = Label(text="is equal to 0 Km")
my_label2.grid(column=3, row=3)

my_btn = Button(text="Convert", command=calculate)
my_btn.grid(column=4, row=4)

window.mainloop()
