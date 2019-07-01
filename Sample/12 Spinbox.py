from tkinter import *
from tkinter.font import *

root = Tk()

# create font
ftTimes = Font(family='Times', size=12, weight=BOLD)

# create a label to display message.
label_text = StringVar()
label = Label(root, textvariable=label_text)
label.grid(row=2, column=0, columnspan=2, sticky=E + W)


# value changed handling.
def spin_changed(*args):
    # get current value and set to label.
    label_text.set(tb.get())

# create a Radiobutton for Teacher.
tb = Spinbox(root,values=('Teacher', 'Student', 'Worker'),
             state='readonly',
             background="#ffffa0",foreground="#ff0000",
             activebackground="#a0ffa0",
             command=spin_changed, font=ftTimes)
tb.grid(row=0, column=0, columnspan=1, sticky=W)

# control variable of value spinbox.
vb_var = StringVar()
vb_var.set('0.6')

def isOkay(text):
    print(text)
    if text == '-':
        return True
    if len(text)==0:
        return True
    value = int(float(text) * 100)
    if -100 <= value <= 100:
        if value % 20 == 0:
            return True
    return False

okayCommand=root.register(isOkay)

# create a value spinbox.
vb = Spinbox(root,
             from_=-1.0,to=1.0,increment=0.2,wrap=True,
             background="#ffffa0", foreground="#ff0000",
             activebackground="#a0ffa0",
             textvariable=vb_var, font=ftTimes,
             validate='key',
             validatecommand=(okayCommand, '%P'))
vb.grid(row=1, column=0, columnspan=1, sticky=W)

def var_changed(*args):
    label_text.set(vb_var.get())

# set variable observer.
vb_var.trace_variable('w', var_changed)

# run main loop.
root.mainloop()
