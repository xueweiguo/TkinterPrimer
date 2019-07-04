from tkinter import *
from tkinter.font import *

root = Tk()

#font setting.
font_size = 12
font_family = ['Times','Arial', 'Roma']
font_weight = ['bold', 'normal']
font_slant = ['italic','roman','normal']

# create font
label_font = Font(family=font_family[0], size=font_size,
                  weight=font_weight[0], slant=font_slant[0])

# create a label to display message.
label = Label(root, text='ScaleTest', font=label_font, foreground="#000000",)
label.grid(row=0, column=0, columnspan=4, sticky=E + W)

#toggle underline.
def toggle_underline():
    under_line = label_font.cget('underline')
    label_font.config(underline=not under_line)

# create check button.
ub = Checkbutton(root,text="Underline",command=toggle_underline)
ub.grid(row=1, column=0, columnspan=2)

#toggle overstrike.
def toggle_overstrike():
    over_strike = label_font.cget('overstrike')
    label_font.config(overstrike=not over_strike)

#create check button.
ob = Checkbutton(root,text="Overstrike",command=toggle_overstrike)
ob.grid(row=1, column=1, columnspan=2)

#label of readonly spinbox.
Label(root, text='Family').grid(row=2,column=0, sticky=E)

def family_changed():
    label_font.config(family=fb.get())

# create a value spinbox.
fb = Spinbox(root, values=font_family, wrap=True, state='readonly',
             command=family_changed)
fb.grid(row=2, column=1, columnspan=2, sticky=W+E)

#label of weight spinbox.
Label(root, text='Weight').grid(row=3,column=0, sticky=E)

def weight_changed():
    label_font.config(weight=wb.get())

# create a weight spinbox.
wb = Spinbox(root, values=font_weight, wrap=True, state='readonly',
             command=weight_changed)
wb.grid(row=3, column=1, columnspan=3, sticky=W+E)

# create a lable of size scale.
Label(root, text='Size').grid(row=4,column=0, sticky=E)

def scale_changed(value):
    label_font.config(size=value)

# create font size scale.
fs = Scale(root, relief=GROOVE, orient=HORIZONTAL,
           from_=10, to_=32, resolution=1,
           command=scale_changed)
fs.grid(row=4, column=1, columnspan=3, sticky=W+E)

# create a lable of gray scale.
Label(root, text='Gray').grid(row=5,column=0, sticky=E)

def gray_changed(value):
    value = '{:02x}'.format(int(value))
    value = '#'+value+value+value
    label.config(foreground=value)

# create gray scale.
cs = Scale(root, relief=GROOVE, orient=HORIZONTAL,
           from_=0, to_=255, resolution=1,
           command=gray_changed)
cs.grid(row=5, column=1, columnspan=3, sticky=W+E)

# run main loop.
root.mainloop()
