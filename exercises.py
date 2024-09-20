from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=100)


def click_btn():
    # my_label.config(text="Clicked!")
    new_text = my_input.get()
    my_label.config(text=new_text)


my_label = Label(text="Hello World", font=("Arial", 24, "bold"))
my_label.config(text="Sample")
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_btn1 = Button(text="Click", command=click_btn)
my_btn1.grid(column=1, row=1)

my_btn2 = Button(text="Click", command=click_btn)
my_btn2.grid(column=2, row=0)

my_input = Entry(width=10)
my_input.grid(column=3, row=2)


def add(*args):
    print(args)
    my_sum = 0
    for n in args:
        my_sum += n
    return my_sum


print(add(1, 2, 3, 4))


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

window.mainloop()
