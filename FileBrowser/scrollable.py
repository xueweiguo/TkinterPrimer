from tkinter import *
from tkinter.ttk import *


def scrollable(master, w_type, **kwargs):
    size_grip = kwargs.get('size_grip')
    if size_grip:
        kwargs.pop('size_grip')
    frame = Frame(master)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    widget = w_type(frame, **kwargs)
    widget.grid(row=0, column=0, sticky='nsew')
    scroll_y = Scrollbar(frame, orient=VERTICAL, command=widget.yview)
    scroll_y.grid(row=0, column=1, sticky=N + S)
    widget['yscrollcommand'] = scroll_y.set
    scroll_x = Scrollbar(frame, orient=HORIZONTAL, command=widget.xview)
    scroll_x.grid(row=1, column=0, sticky=E + W)
    widget['xscrollcommand'] = scroll_x.set
    if size_grip:
        Sizegrip(frame).grid(row=1, column=1)
    return frame,widget

