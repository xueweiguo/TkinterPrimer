from tkinter import *
from tkinter.font import *

root = Tk()

# create font
ftTimes = Font(family='Times', size=24, weight=BOLD, slant=ITALIC)

# create a button to change state.
state_button = Button(root,text="ColorButton",
       background="#ffffa0",foreground="#ff0000",
       activebackground="#a0ffa0",activeforeground="#0000ff",
       font=ftTimes, height=2)
state_button.grid(row=0, column=0)

# change state function.
def change_state():
    state = state_button.cget('state')
    if state==DISABLED:
        state_button.config(state=NORMAL)
    elif state==NORMAL:
        state_button.config(state=ACTIVE)
    else:
        state_button.config(state=DISABLED)

# change state button.
Button(root,text="<<ChangeState", command=change_state).grid(row=0, column=1)

# create a button with padx and pady.
Button(root,text="PadButton", font=ftTimes,
       padx=50, pady=20).grid(row=1, column=0, columnspan=2)

# create a button with multiple line text.
Button(root,text="This is a MultilineButton.",
       wraplength=220, font= ftTimes).grid(row=2, column=0, columnspan=2)

# run main loop.
root.mainloop()
