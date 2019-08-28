from tkinter import *
from tkinter.ttk import *

class Timer:
    def __init__(self, wnd, ms, call):
        self.__wnd = wnd
        self.__ms = ms
        self.__call = call
        self.__running = False

    def start(self):
        if not self.__running:
            self.__wnd.after(0, self.__on_timer)
            self.__running = True

    def stop(self):
        if self.__running:
            self.__running = False

    def set_timer(self, ms):
        self.__ms = ms

    def get_timer(self):
        return self.__ms

    def is_running(self):
        return self.__running

    def __on_timer(self):
        if self.__running:
            self.__call()
            self.__wnd.after(self.__ms, self.__on_timer)

# create the main window
root = Tk()

menu = Menubutton(root, text="File")
menu.grid(row=0, column=0, sticky=W)
file_menu = Menu(menu, tearoff=0)
menu.config(menu=file_menu)
file_menu.add_command(label="Exit", command=exit)

p_value = IntVar()
p_value.set(0)
progress = Progressbar(root, maximum=100, variable=p_value)
progress.grid(row=1, column=0, columnspan=3, sticky='ew')

def on_timer():
    if p_value.get() < progress.cget('maximum'):
        p_value.set(p_value.get() + 1)
    else:
        timer.stop()

timer=Timer(root, 100, on_timer)

c_var = StringVar()
c_var.set(str(timer.get_timer()))
def t_changed(*args):
    timer.set_timer(int(c_var.get()))
c_var.trace_variable('w', t_changed)

time_values=['50', '100', '200']
c_box = Combobox(root, values=time_values, textvariable=c_var, state='readonly')
c_box.grid(row=2, column=0)

start_btn = Button(root, text='Start', command=timer.start)
start_btn.grid(row=2, column=1)

def stop_timer():
    timer.stop()
    p_value.set(0)
stop_btn = Button(root, text='Stop', command=stop_timer)
stop_btn.grid(row=2, column=2)

root.mainloop()