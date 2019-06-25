from tkinter import *
from tkinter.font import *

root = Tk()

# create font
ftTimes = Font(family='Times', size=12, weight=BOLD)

# create Label
label_text = StringVar()
label = Label(root, textvariable=label_text)
label.grid(row=2, column=0, columnspan=2, sticky=E + W)

# control variable
rb_var = StringVar()
rb_var.set('T')

# create a Radiobutton for Teacher.
rbt = Radiobutton(root,text="Teacher",
                  background="#ffffa0",foreground="#ff0000",
                  activebackground="#a0ffa0",activeforeground="#0000ff",
                  variable=rb_var, value='T',
                  font=ftTimes, height=1)
rbt.grid(row=0, column=0, columnspan=1, sticky=W)

# create a Radiobutton for Student.
rbs = Radiobutton(root,text="Student",
                  background="#ffffa0",foreground="#ff0000",
                  activebackground="#a0ffa0",activeforeground="#0000ff",
                  variable=rb_var, value='S',
                  font=ftTimes, height=1)
rbs.grid(row=1, column=0, columnspan=1, sticky=W)


def var_changed(*args):
    label_text.set(rb_var.get())

# set variable observer.
rb_var.trace_variable('w', var_changed)

# run main loop.
root.mainloop()
