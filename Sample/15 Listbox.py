from tkinter import *
from tkinter.font import *

root = Tk()

# create font
ftiTimes = Font(family='Times', size=24, weight=BOLD, slant=ITALIC)

# create a label to change state.
label = Label(root,text="ColorLabel",
       background="#ffffa0",foreground="#ff0000",
       activebackground="#a0ffa0",activeforeground="#0000ff",
       font=ftiTimes, height=1, width=20)
label.grid(row=0, column=0, columnspan=4)

# start and run mainloop
root.mainloop()