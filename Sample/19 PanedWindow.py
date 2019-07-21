from tkinter import *
from tkinter.font import *

# create the main window
root = Tk()

paned_window = PanedWindow(root, background="#a0ffa0")

# create font
ftiTimes = Font(family='Times', size=24, weight=BOLD)

# create a listbox for demo.
lb = Listbox(paned_window,
             activestyle='dotbox',
             bg="#ffffa0",fg="#ff0000",
             disabledforeground="#3f3f3f",
             highlightbackground="#0000ff",
             font=ftiTimes,
             height=10, width=20)

# add items
for i in range(0,20):
    lb.insert(END, str(i))

# bind event
lb.bind('<<ListboxSelect>>',
        lambda e: label.config(text=str(lb.curselection())))
paned_window.add(lb)

edit_area = Frame(paned_window)

# create text widget.
text = Text(edit_area,
            background="#a0ffa0", foreground="#000000",
            wrap=NONE)
text.grid(row = 0, column = 0, sticky=W+N+E+S)

scroll_ty = Scrollbar(edit_area, orient=VERTICAL, command=text.yview)
scroll_ty.grid(row=0, column=1, sticky=N+S)
text['yscrollcommand']=scroll_ty.set

scroll_tx = Scrollbar(edit_area, orient=HORIZONTAL, command=text.xview)
scroll_tx.grid(row=1, column=0, sticky=E+W)
text['xscrollcommand']=scroll_tx.set

edit_area.grid_rowconfigure(0, weight=1)
edit_area.grid_columnconfigure(0, weight=1)

paned_window.add(edit_area, sticky=W+N+E+S, padx=2, pady=2)

paned_window.grid(row = 0, column = 0, sticky=N+S+W+E)

label=Label(root)
label.grid(row=1, column=0)

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()