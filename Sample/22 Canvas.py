from tkinter import *
from tkinter.font import *
from enum import Enum

# create the main window
root = Tk()

# config go pan
space = 30
pan_size = 13

# create canvas
canvas = Canvas(root, height= space * pan_size, width= space * pan_size)
canvas.grid(row=0, column=0)

# crate pan
canvas.create_rectangle(space / 2, space / 2, 
                        space * pan_size - space / 2, space * pan_size - space / 2,
                        fill = '#eeaa40')
# draw horizental lines
for r in range(0, pan_size):
    canvas.create_line(space / 2, space / 2 + r * space, 
                       space * pan_size - space / 2, space / 2 + r * space)
# draw vertical lines
for c in range(0, pan_size):
    canvas.create_line(space / 2 + c * space, space / 2, 
                       space / 2 + c * space, space * pan_size - space / 2)


#color enum value
class GoColor(Enum):
    WHITE = 0
    BLACK = 1

# create font
ftTimes = Font(family='Times', size=12)

# add go
def set_go(row, col, color, number=0):
    r = 11
    go_color = 'white'
    font_color = 'black'
    if color==GoColor.BLACK:
        go_color = 'black'
        font_color = 'white'
    # add go shape
    canvas.create_oval(space / 2 + col * space - r, space / 2 + row * space - r,
                       space / 2 + col * space + r, space / 2 + row * space + r,
                       fill=go_color)
    # add number
    if number>0:
        canvas.create_text(space / 2 + col * space, space / 2 + row * space,
                           font=ftTimes, fill=font_color,
                           text=str(number))

# add gos.
set_go(3, 10, GoColor.BLACK)
set_go(3, 8, GoColor.WHITE)
set_go(5, 10, GoColor.BLACK, 1)
set_go(2, 10, GoColor.WHITE, 2)
set_go(2, 11, GoColor.BLACK, 3)
set_go(2, 9, GoColor.WHITE, 4)
set_go(1, 11, GoColor.BLACK, 5)
set_go(2, 4, GoColor.WHITE, 6)

#run the mainloop.
root.mainloop()