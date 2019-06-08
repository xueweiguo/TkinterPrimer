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

# change state function.
def change_state():
    state = label.cget('state')
    if state==DISABLED:
        label.config(state=NORMAL)
    elif state==NORMAL:
        label.config(state=ACTIVE)
    else:
        label.config(state=DISABLED)

# change state button.
Button(root,text="State", command=change_state).grid(row=1, column=0, sticky=E+W)

# change label height function.
def change_height():
    current_height = label.cget('height')
    if current_height == 4:
        current_height = 1
    else:
        current_height = current_height + 1
    label.config(height=current_height)

# change state button.
Button(root,text="Height", command=change_height).grid(row=1, column=1, sticky=E+W)

# change state justify.
def change_width():
    width = label.cget('width')
    if width == 20:
        width = 1
    else:
        width = width + 1
    label.config(width=width)

# change state button.
Button(root,text="Width", command=change_width).grid(row=1, column=2, sticky=E+W)

# change label_text
def change_text():
    text = label.cget('text')
    if text=="ColorLabel":
        label.config(text='Demo')
    else:
        label.config(text='ColorLabel')

# change state button.
Button(root,text="Text", command=change_text).grid(row=1, column=3, sticky=E+W)

ftTimes = Font(family='Times', size=12, weight=BOLD)

str_var = StringVar()
str_var.set("You can limit the number of characters in each"
            "line by seting this option tothedesirednumber.")

# create a label to change state.
m_label = Label(root,font=ftTimes, height=3, wraplength=250,
                textvariable=str_var)
m_label.grid(row=2, column=0, columnspan=4)

# change text underline.
def prev_underline():
    text = m_label.cget('text')
    underline = m_label.cget('underline')
    if underline == -1:
        m_label.config(underline=len(text) - 1)
    else:
        underline = underline - 1
        if underline == -1:
            m_label.config(underline=len(text) - 1)
        else:
            m_label.config(underline=underline)

# change state button.
Button(root,text='PrevChar', command=prev_underline).grid(row=3, column=0, sticky=E+W)

# change text underline.
def next_underline():
    text = m_label.cget('text')
    underline = m_label.cget('underline')
    if underline == -1:
        m_label.config(underline=0)
    else:
        underline = underline + 1
        if underline>=len(text):
            m_label.config(underline=0)
        else:
            m_label.config(underline=underline)

# change state button.
Button(root,text='NextChar', command=next_underline).grid(row=3, column=1, sticky=E+W)

# delete char.
def delete_char():
    text = str_var.get()
    underline = m_label.cget('underline')
    if underline >=0 and underline < len(text):
        str_var.set(text[0 : underline] + text[underline + 1:])

# change state button.
Button(root,text='DeleteChar', command=delete_char).grid(row=3, column=2, sticky=E+W)

# change state justify.
def change_justify():
    justify = m_label.cget('justify')
    if justify==LEFT:
        m_label.config(justify=CENTER)
    elif justify==CENTER:
        m_label.config(justify=RIGHT)
    else:
        m_label.config(justify=LEFT)

# change state button.
Button(root,text="Justify", command=change_justify).grid(row=3, column=3, sticky=E+W)

# run main loop.
root.mainloop()
