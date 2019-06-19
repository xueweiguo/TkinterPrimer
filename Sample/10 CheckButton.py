from tkinter import *
from tkinter.font import *

root = Tk()

# create font
ftiTimes = Font(family='Times', size=24, weight=BOLD, slant=ITALIC)

label = Label(root)
label.grid(row=2, column=0, columnspan=2, sticky=E + W)

# control variable
cb1_var = IntVar()
cb1_var.set(0)

# A procedure to be called every time
# the user changes the state of this checkbutton.
def on_check():
    label.config(text=cb1_var.get())

# create a CheckButton.
cb1 = Checkbutton(root,text="CheckButton",
        background="#ffffa0",foreground="#ff0000",
        activebackground="#a0ffa0",activeforeground="#0000ff",
        variable=cb1_var,
        onvalue=5, offvalue=-5,
        command=on_check,
        font=ftiTimes, height=1, width=10)
cb1.grid(row=0, column=0, columnspan=2)

# 通过修改变量值修改CheckButton状态
def toggle_by_var():
    sel = cb1_var.get()
    if sel == 0:
        cb1_var.set(5) #必须和onvalue一致
    else:
        cb1_var.set(0)

Button(root, text='toggle by var', command=toggle_by_var).grid(row=1, column=0, sticky=E+W)

# 通过调用toggle函数修改CheckButton状态
def toggle_by_fun():
    cb1.toggle()

Button(root, text='toggle_by_fun', command=toggle_by_fun).grid(row=1, column=1, sticky=E+W)

# run main loop.
root.mainloop()
