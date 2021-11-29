from tkinter import *
from tkinter import font
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title('Vanja\'s Clock App')


def time():
    time_string = strftime('%H:%M:%S %p')
    label.config(text=time_string)
    label.after(1000, time)


label = Label(root, font=('DS-Digital', 80),
              back='#2E4C6D', foreground='#DADDFC')
label.pack(anchor='center')

time()

mainloop()