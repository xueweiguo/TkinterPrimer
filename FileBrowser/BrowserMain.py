from tkinter import *
from tkinter.ttk import *

from scrollable import *
from DirView import *
from FileList import *

root = Tk()
root.title('Python FileBrowser V1.0')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

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

theme_menu = Menu(top_menu, tearoff=False)
top_menu.add_cascade(label='Theme', menu=theme_menu)

theme = StringVar()
theme.set(Style().theme_use())
for t in Style().theme_names():
    theme_menu.add_radiobutton(label=t, value=t, variable=theme)

def theme_changed(*arg):
    Style().theme_use(theme.get())
theme.trace_variable('w', theme_changed)

paned_window = PanedWindow(root, orient=HORIZONTAL)
paned_window.grid(row=0, column=0, sticky='eswn')

tree_area, tree_view = scrollable(paned_window, DirView)
paned_window.add(tree_area)

detail_area, list_view = scrollable(paned_window, FileList, tree_view=tree_view)
paned_window.add(detail_area)

tree_view.bind('<<TreeviewSelect>>', list_view.select_node)

root.mainloop()