from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)


def convert():
    num = float(my_input.get())
    num *= 1.6
    label_num.config(text=f"{num}")


my_input = Entry(width=5)
my_input.insert(END, string="0")
my_input.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)
label_equal.config(padx=10, pady=10)

label_num = Label(text="0")
label_num.grid(column=1, row=1)
label_num.config(padx=10, pady=10)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)
label_equal.config(padx=10, pady=10)

my_btn = Button(text="Convert", command=convert)
my_btn.grid(column=1, row=2)

window.mainloop()
