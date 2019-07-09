from tkinter import *
from tkinter.font import *

root = Tk()

# create font
ftiTimes = Font(family='Times', size=24, weight=BOLD)

# create a listbox for demo.
lb = Listbox(root,
             activestyle='dotbox',
             bg="#ffffa0",fg="#ff0000",
             disabledforeground="#3f3f3f",
             highlightbackground="#0000ff",
             font=ftiTimes,
             height=10, width=20)

# add items
for i in range(0,20):
    lb.insert(END, str(i))

# bind event
lb.bind('<<ListboxSelect>>',
        lambda:label.config(text=str(lb.curselection())))
lb.grid(row=0, column=0, columnspan=3, sticky=W+E)

# create a Spinbox to change state.
st_spin = Spinbox(root,
                  values=('disabled', 'normal'),
                  state='readonly',
                  command=lambda:lb.config(state=st_spin.get()))
st_spin.grid(row=1, column=0, columnspan=1, sticky=W)

# create a Spinbox to change activestyle.
as_spin = Spinbox(root,
                  values=('underline', 'dotbox', 'none'),
                  state='readonly',
                  command=lambda:lb.config(activestyle=as_spin.get()))
as_spin.grid(row=1, column=1, columnspan=1, sticky=W)

# create a Spinbox to change select mode.
sm_spin = Spinbox(root,
                  values=('browse', 'single', 'multiple', 'extended'),
                  state='readonly',
                  command=lambda:lb.config(selectmode=sm_spin.get()))
sm_spin.grid(row=1, column=2, columnspan=1, sticky=W)

label=Label(root)
label.grid(row=2, column=0, columnspan=4)

# start and run mainloop
root.mainloop()