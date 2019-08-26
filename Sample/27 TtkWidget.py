from tkinter import *
from tkinter.ttk import *

# create the main window
root = Tk()

s_frame = LabelFrame(root, text='Standard Button')
s_frame.grid(row=0, column=0)
s_button = Button(s_frame, text='Button', width=12)
s_button.grid(row=0, column=0)

c_frame = LabelFrame(root, text='CheckButton')
c_frame.grid(row=1, column=0)

def d_changed(*args):
    c_text.set('Value={}{}{}{}'.format(d3.get(),d2.get(),d1.get(),d0.get()))

c_text = StringVar()
c_text.set('Value=0000')
c_label = Label(c_frame, textvariable=c_text, width=10)
c_label.grid(row=0, column=0)
d3 = IntVar()
d3.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D3', variable=d3)
c_button.grid(row=0, column=1)
d2 = IntVar()
d2.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D2', variable=d2)
c_button.grid(row=0, column=2)
d1 = IntVar()
d1.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D1',variable=d1)
c_button.grid(row=0, column=3)
d0 = IntVar()
d0.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D0', variable=d0)
c_button.grid(row=0, column=4)
d3.set(0)
d2.set(0)
d1.set(0)
d0.set(0)

r_frame = LabelFrame(root, text='RadioButton')
r_frame.grid(row=2, column=0)

r_label = Label(r_frame, text='Value=0', width=10)
r_label.grid(row=0, column=0)
def r_changed(*arg):
    r_label.configure(text='Value='+str(r_value.get()))
r_value = IntVar()
r_value.trace_variable('w', r_changed)
r_value.set(0)
r_button = Radiobutton(r_frame, text='0 ', variable=r_value, value=0)
r_button.grid(row=0, column=1)
r_button = Radiobutton(r_frame, text='1 ', variable=r_value, value=1)
r_button.grid(row=0, column=2)
r_button = Radiobutton(r_frame, text='2 ', variable=r_value, value=2)
r_button.grid(row=0, column=3)
r_button = Radiobutton(r_frame, text='3 ', variable=r_value, value=3)
r_button.grid(row=0, column=4)
root.mainloop()