from tkinter import *
from tkinter.font import *

# create the main window
root = Tk()

top_menu = Menu(root)
root.config(menu=top_menu)

edit_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='Edit', menu=edit_menu)
format_menu = Menu(top_menu)
top_menu.add_cascade(label='Format', menu=format_menu)

text_enable = IntVar()
text_enable.set(1)

# change state function.
def enable_text():
    text_enable.set(1)

# change state button.
eb = Radiobutton(root,text="Enable", width=8, command=enable_text,
                 value=1, variable=text_enable)
eb.grid(row=1, column=0, sticky=E+W)
edit_menu.add_radiobutton(label='Enable', command=enable_text,
                          value=1, variable=text_enable)

# change state function.
def disable_text():
    text_enable.set(0)

# change state button.
eb = Radiobutton(root,text="Disable", width=8, command=disable_text,
                 value=0, variable=text_enable)
eb.grid(row=1, column=1, sticky=E+W)
edit_menu.add_radiobutton(label='Disable', command=disable_text,
                      value=0, variable=text_enable)

def var_changed(*args):
    if text_enable.get():
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
db.grid(row=1, column=2, sticky=E+W)
edit_menu.add_radiobutton(label='Delete', command=delete_selection)

# undo button
undo = Button(root, text='Undo', width = 8, command=lambda:text.edit_undo())
undo.grid(row=1, column = 3, sticky=E+W)
edit_menu.add_radiobutton(label='Undo', command=lambda:text.edit_undo())

#redo button
redo = Button(root, text='Redo', width = 8, command=lambda:text.edit_redo())
redo.grid(row=1, column = 4, sticky=E+W)
edit_menu.add_radiobutton(label='Redo', command=lambda:text.edit_redo())

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
    fb = Button(root,
                text="Format" + str(i),
                width = 8,
                command=lambda v=i : format(v))
    format_menu.add_command(label="Format" + str(i),
                           command=lambda v=i : format(v))
    fb.grid(row=2, column=i, sticky=E+W)

# create text widget.
text = Text(root,
            undo=True,
            background="#a0ffa0", foreground="#000000",
            height = 10)
text.grid(row=3 , column=0, columnspan=8)

# delete selection.
def tags():
    for name in text.tag_names():
        print(name, ":", text.tag_ranges(name))

# run main loop.
root.mainloop()