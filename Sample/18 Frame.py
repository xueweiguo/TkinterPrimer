from tkinter import *
from tkinter.font import *

# create the main window
root = Tk()

edit_frame = Frame(root)

# change state function.
def change_state():
    state = text.cget('state')
    if state=='disabled':
        text.config(state='normal')
        text.config(background='#a0ffa0')
    else:
        text.config(state='disabled')
        text.config(background='#efefef')


# change state button.
eb = Button(edit_frame,text="Enable", width=8, command=change_state)
eb.grid(row=0, column=0, sticky=E+W)

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
db = Button(edit_frame,text="Delete", width = 8, command=delete_selection)
db.grid(row=0, column=1, sticky=E+W)

# undo button
undo = Button(edit_frame, text='Undo', width = 8, command=lambda:text.edit_undo())
undo.grid(row=0, column = 2, sticky=E+W)

#redo button
redo = Button(edit_frame, text='Redo', width = 8, command=lambda:text.edit_redo())
redo.grid(row=0, column = 3, sticky=E+W)

edit_frame.grid(row=0, column=0, sticky=W)

format_frame = Frame(root)

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

# delete selection button.
for i in range(0, 4):
    fb = Button(format_frame,
                text="Format" + str(i),
                width = 8,
                command=lambda v=i : format(v))
    fb.grid(row=1, column=i, sticky=E+W)

format_frame.grid(row=1, column=0, sticky=W)

# create text widget.
text = Text(root,
            undo=True,
            background="#a0ffa0", foreground="#000000",
            height = 10)
text.grid(row=2 , column=0)

# run main loop.
root.mainloop()