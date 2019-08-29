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

root = Tk()
root.resizable(False, False)
root.title('Notebook Demo V1.0')

notebook = Notebook(root)
notebook.grid(row=0, column=0)

tab1 = Frame(notebook)
s_frame = LabelFrame(tab1, text='Standard Button')
s_frame.grid(row=0, column=0)
s_button = Button(s_frame, text='Button', width=12)
s_button.grid(row=0, column=0)

c_frame = LabelFrame(tab1, text='CheckButton')
c_frame.grid(row=1, column=0)

def d_changed(*args):
    c_text.set('Value={}{}{}{}'.format(d3.get(),d2.get(),d1.get(),d0.get()))

c_text = StringVar()
c_text.set('Value=0000')
c_label = Label(c_frame, textvariable=c_text, width=10)
c_label.grid(row=0, column=0)
d3 = IntVar()
d3.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D3', variable=d3)
c_button.grid(row=0, column=1)
d2 = IntVar()
d2.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D2', variable=d2)
c_button.grid(row=0, column=2)
d1 = IntVar()
d1.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D1',variable=d1)
c_button.grid(row=0, column=3)
d0 = IntVar()
d0.trace_variable('w', d_changed)
c_button = Checkbutton(c_frame, text='D0', variable=d0)
c_button.grid(row=0, column=4)
d3.set(0)
d2.set(0)
d1.set(0)
d0.set(0)

r_frame = LabelFrame(tab1, text='RadioButton')
r_frame.grid(row=2, column=0)

r_label = Label(r_frame, text='Value=0', width=10)
r_label.grid(row=0, column=0)
def r_changed(*arg):
    r_label.configure(text='Value='+str(r_value.get()))
r_value = IntVar()
r_value.trace_variable('w', r_changed)
r_value.set(0)
r_button = Radiobutton(r_frame, text='0 ', variable=r_value, value=0)
r_button.grid(row=0, column=1)
r_button = Radiobutton(r_frame, text='1 ', variable=r_value, value=1)
r_button.grid(row=0, column=2)
r_button = Radiobutton(r_frame, text='2 ', variable=r_value, value=2)
r_button.grid(row=0, column=3)
r_button = Radiobutton(r_frame, text='3 ', variable=r_value, value=3)
r_button.grid(row=0, column=4)
notebook.add(tab1, text='Demo1')

tab2 = Frame(notebook)

p_value = IntVar()
p_value.set(0)
progress = Progressbar(tab2, maximum=100, variable=p_value)
progress.grid(row=1, column=0, columnspan=3, sticky='ew')

def on_timer():
    if p_value.get() < progress.cget('maximum'):
        p_value.set(p_value.get() + 1)
    else:
        timer.stop()

timer=Timer(tab2, 100, on_timer)

c_var = StringVar()
c_var.set(str(timer.get_timer()))
def t_changed(*args):
    timer.set_timer(int(c_var.get()))
c_var.trace_variable('w', t_changed)

time_values=['50', '100', '200']
c_box = Combobox(tab2, values=time_values, textvariable=c_var, state='readonly')
c_box.grid(row=2, column=0)

start_btn = Button(tab2, text='Start', command=timer.start)
start_btn.grid(row=2, column=1)

def stop_timer():
    timer.stop()
    p_value.set(0)
stop_btn = Button(tab2, text='Stop', command=stop_timer)
stop_btn.grid(row=2, column=2)

notebook.add(tab2, text='Demo2')

root.mainloop()
