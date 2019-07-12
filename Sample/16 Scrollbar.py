import copy
from tkinter import *
from tkinter.font import *

root = Tk()

label = Label(root, width = 50)
label.grid(row=0, column=0, columnspan=2)

def on_scroll(*args):
    pos = scroll_bar.get()
    print(pos)
    page = 0.1
    if args[0]=='scroll':
        if args[2]=='units':
            first =  pos[0] + int(args[1])* 0.01
        elif args[2]=='pages':
            first =  pos[0]  + int(args[1])* 0.1
        else:
            first = 0
    elif args[0]=='moveto':
        first = float(args[1])
    else:
        first = 0
    scroll_bar.set(first,first + 0.1)
    label.config(text=str(args))

scroll_bar = Scrollbar(root, orient = HORIZONTAL, command=on_scroll)
scroll_bar.grid(row = 1, column=0, columnspan=2, sticky=W+E)

class ScrollbarEx(Scrollbar):
    def __init__(self, master, **args):
        arg_dict = copy.copy(args)
        try:
            self.min = arg_dict.pop('min')
        except KeyError:
            self.min = 0
        try:
            self.max = arg_dict.pop('max')
        except KeyError:
            self.max = 1
        try:
            self.page = arg_dict.pop('page')
        except KeyError:
            self.page = 0.1
        try:
            self.unit = arg_dict.pop('unit')
        except KeyError:
            self.unit = 0.01
        try:
            self.on_scroll = arg_dict.pop('on_scroll')
        except KeyError:
            pass
        arg_dict.update(command = self.scroll_handler)
        Scrollbar.__init__(self, master, arg_dict, )
        self.scroll_handler()

    def scroll_handler(self, *args):
        pos = self.get()
        span = self.max - self.min
        page = self.page / span
        unit = self.unit / span
        first = 0
        if args:
            if args[0]=='scroll':
                if args[2]=='units':
                    first =  pos[0] + int(args[1])* unit
                elif args[2]=='pages':
                    first =  pos[0]  + int(args[1])* page
                else:
                    first = 0
            elif args[0]=='moveto':
                first = float(args[1])
            else:
                first = 0
        self.set(first, first + page)
        if self.on_scroll:
            self.on_scroll(int(self.min + first * span),
                           int(self.min + first * span + self.page))


def on_scroll_ex(first, last):
    label.config(text="first={},last={}".format(first, last))

scrollbar_ex = ScrollbarEx(root, min=0, max=100,
                           page=10, unit=2,
                           on_scroll=on_scroll_ex,
                           orient = HORIZONTAL)
scrollbar_ex.grid(row=2, column=0, columnspan=2, sticky=W+E)

# start and run mainloop
root.mainloop()