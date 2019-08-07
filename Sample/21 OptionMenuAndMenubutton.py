from tkinter import *
from tkinter.font import *

# create the main window
root = Tk()

text_enable = StringVar()
text_enable.set('Enable ')

# change state function.
def enable_text():
    text_enable.set('Enable')

# change state function.
def disable_text():
    text_enable.set('Disable')

enable_menu = OptionMenu(root, text_enable, 'Enable ', 'Disable')
enable_menu.grid(row = 0, column = 0, sticky=E+W)

def var_changed(*args):
    if text_enable.get() == 'Enable ':
        text.config(state='normal')
        text.config(background='#a0ffa0')
    else:
        text.config(state='disabled')
        text.config(background='#efefef')
# set variable observer.
text_enable.trace_variable('w', var_changed)

# delete selection.
def delete_selection():
    try:
        sel_from = text.index(SEL_FIRST)
        sel_to = text.index(SEL_LAST)
        # delete the selection.
        text.delete(sel_from, sel_to)
    except TclError:
        pass

# delete selection button.
db = Button(root,text="Delete", width = 8, command=delete_selection)
db.grid(row=0, column=1, sticky=E+W)

def undo():
    try:
        text.edit_undo()
    except Exception as e:
        pass

# undo button
undo = Button(root, text='Undo', width = 8, command=undo)
undo.grid(row=0, column = 2, sticky=E+W)

def redo():
    try:
        text.edit_redo()
    except Exception as e:
        pass

#redo button
redo = Button(root, text='Redo', width = 8, command=redo(), relief=RAISED)
redo.grid(row=0, column = 3, sticky=E+W)

# create fonts
fonts = [
    Font(family='SimHei', size=20, weight=BOLD),
    Font(family='SimHei', size=16),
    Font(family='SimSun', size=12, weight=BOLD),
    Font(family='SimSun', size=12)
    ]

# delete selection.
def format(index):
    tag_name = 'Format' + str(index)
    try:
        sel_from = text.index(SEL_FIRST)
        sel_to = text.index(SEL_LAST)
        for name in text.tag_names():
            text.tag_remove(name, sel_from, sel_to)
        text.tag_add(tag_name, sel_from, sel_to)
        # set format at first time.
        range_count = len(text.tag_ranges(tag_name))
        if range_count == 2:
            text.tag_config(tag_name, font=fonts[index])
    except TclError:
        pass

menu_button = Menubutton(root, text='Format', relief=RAISED)
menu_button.grid(row=0, column=4, sticky=E+W)
format_menu = Menu(menu_button, tearoff=0)
menu_button.config(menu=format_menu)

# delete selection button.
for i in range(0, 4):
    format_menu.add_command(label="Format" + str(i), command=lambda v=i : format(v))

# create text widget.
text = Text(root,
            undo=True,
            background="#a0ffa0", foreground="#000000",
            height = 10)
text.grid(row=3 , column=0, columnspan=8)

# run main loop.
root.mainloop()