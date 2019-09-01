from tkinter import *
from tkinter.font import *
from tkinter.ttk import *

root = Tk()
root.title('Tkinter Sizegrip Demo V1.0')

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.maxsize(width=screen_w, height=screen_h)
rw = int(screen_w / 2)
rh = int(screen_h / 2)
root.geometry('{}x{}+{:g}+{:g}'.format(rw, rh, rw / 2, rh / 2))

top_menu = Menu(root)
root.config(menu=top_menu)

file_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

edit_area = Frame(root)
edit_area.grid(row=1, column=0)
# create text widget.
font = Font(family='Arial', size=15),
text = Text(edit_area, font=font, wrap=NONE)
text.config(width=int(text['width']* screen_w / text.winfo_reqwidth()),
            height=int(text['height']* screen_h / text.winfo_reqheight()))
text.grid(row=0, column=0, sticky='nsew')

scroll_ty = Scrollbar(edit_area, orient=VERTICAL, command=text.yview)
scroll_ty.grid(row=0, column=1, sticky=N+S)
text['yscrollcommand']=scroll_ty.set

scroll_tx = Scrollbar(edit_area, orient=HORIZONTAL, command=text.xview)
scroll_tx.grid(row=1, column=0, sticky=E+W)
text['xscrollcommand']=scroll_tx.set

Sizegrip(edit_area).grid(row=1, column=1)

edit_area.grid_rowconfigure(0, weight=1)
edit_area.grid_columnconfigure(0, weight=1)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()