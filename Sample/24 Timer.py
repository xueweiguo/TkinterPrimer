from tkinter import *
from tkinter.font import *
import time

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

    def is_running(self):
        return self.__running

    def __on_timer(self):
        if self.__running:
            self.__call()
            self.__wnd.after(self.__ms, self.__on_timer)

class DigitalClock:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        # create font
        ftDate = Font(family='Times', size=32)
        self.canvas.create_text(width / 2, height / 4,
                                text='',
                                font=ftDate,
                                tag='date')
        ftTime = Font(family='Times', size=64)
        self.canvas.create_text(width / 2, height / 2,
                                text='',
                                font=ftTime,
                                tag='time')

    def update(self):
        time_str = time.strftime('%Y.%m.%d %a', time.localtime())
        self.canvas.itemconfigure('date', text=time_str)
        time_str = time.strftime('%H:%M:%S', time.localtime())
        self.canvas.itemconfigure('time', text=time_str)

# create the main window
root = Tk()
# create canvas
canvas = Canvas(root, height= 400, width= 400)
canvas.grid(row=0, column=0)
clock = DigitalClock(canvas, 400, 400)
timer = Timer(root, 1000, clock.update)
timer.start()
root.mainloop()
timer.stop()