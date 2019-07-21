from tkinter import *
from tkinter.font import *

root = Tk()

label = Label(root, width = 50)
label.grid(row=1, column=0, columnspan=2)

frame1 = LabelFrame(root, text='ScrollListBox')
frame1.grid(row=0, column=0, columnspan=1, sticky=W+E)

# create a listbox for demo.
lb = Listbox(frame1,
             activestyle='dotbox',
             height=8, width=20)

# add items
for i in range(0,20):
    lb.insert(END, str(i))

# bind event
lb.bind('<<ListboxSelect>>',
        lambda e: label.config(text=str(lb.curselection())))
lb.grid(row=0, column=0)

scroll_ly = Scrollbar(frame1, orient=VERTICAL, command=lb.yview)
scroll_ly.grid(row=0, column=1, sticky=N+S)
lb['yscrollcommand']=scroll_ly.set

frame2 = LabelFrame(root, text='ScrollText')
frame2.grid(row=0, column=1, columnspan=1, sticky=W+E+N+S)

# create text widget.
text = Text(frame2, height = 10, width=20, wrap=NONE)
text.grid(row=0, column=0)

scroll_ty = Scrollbar(frame2, orient=VERTICAL, command=text.yview)
scroll_ty.grid(row=0, column=1, sticky=N+S)
text['yscrollcommand']=scroll_ty.set

scroll_tx = Scrollbar(frame2, orient=HORIZONTAL, command=text.xview)
scroll_tx.grid(row=1, column=0, sticky=E+W)
text['xscrollcommand']=scroll_tx.set

# start and run mainloop
root.mainloop()