from tkinter import *
from tkinter.font import *

# create the main window
root = Tk()

# create font
ftTimes = Font(family='Times', size=24, weight=BOLD)

# create a label to change state.
entry = Entry(root,
       background="#a0ffa0",foreground="#000000",
       disabledbackground="#7f7f7f",disabledforeground="#000000",
       font=ftTimes, width=32)
entry.grid(row=0, column=0, columnspan=2)

# create text variable.
str_var = StringVar()
# create a label to change state.
label = Label(root,height=10, justify=LEFT, textvariable=str_var)
label.grid(row=1, column=0, columnspan=2)

# bind event
def OnKeyPress(e):
    print(e)
    current = str_var.get()
    if len(current):
        str_var.set(current + '\n' + str(e))
    else:
        str_var.set(str(e))
entry.bind('<KeyPress>', OnKeyPress)

# change state function.
def change_state():
    state = entry.cget('state')
    if state=='disabled':
        entry.config(state='normal')
    elif state=='normal':
        entry.config(state='readonly')
    else:
        entry.config(state='disabled')

# change state button.
Button(root,text="State", command=change_state).grid(row=2, column=0, sticky=E+W)


# delete selection.
def delete_selection():
    print("INSERT=", entry.index(INSERT), 'ANCHOR=', entry.index(ANCHOR))
    anchor = entry.index(ANCHOR)
    if anchor: # there is a selection
        # current position of the insertion cursor
        insert = entry.index(INSERT)
        sel_from = min(anchor, insert)
        sel_to = max(anchor, insert)
        # delete the selection.
        entry.delete(sel_from, sel_to)

# delete selection button.
Button(root,text="Delete", command=delete_selection).grid(row=2, column=1, sticky=E+W)

# run main loop.
root.mainloop()