from tkinter import *
from tkinter.font import *
import time
import math

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

class Clock:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.digital = True
        self.type = None
        # create font for date.
        ftDate = Font(family='Times', size=32)
        self.canvas.create_text(width / 2, height / 4,
                                text='',
                                font=ftDate,
                                tag='date')
        # create font for time.
        self.ftTime = Font(family='Times', size=64)
        self.set_type('Digital')

    def set_type(self, type):
        if type=='Digital':
            self.canvas.create_text(self.width / 2, self.height / 2,
                                    text='',
                                    font=self.ftTime,
                                    tag='time')
            self.canvas.delete('hour')
            self.canvas.delete('minute')
            self.canvas.delete('second')
            self.canvas.delete('center')
        else:
            self.canvas.delete('time')
            self.canvas.create_line(self.width / 2, self.height / 2,
                                    self.width / 2, self.height / 2,
                                    width=15,
                                    fill='red',
                                    arrow=LAST,
                                    arrowshape=(self.width / 20, self.width / 10, self.width / 40),
                                    tag='hour')
            self.canvas.create_line(self.width / 2, self.height / 2,
                                    self.width / 2, self.height / 2,
                                    width=10,
                                    fill='green',
                                    capstyle=ROUND,
                                    tag='minute')
            self.canvas.create_line(self.width / 2, self.height / 2,
                                    self.width / 2, self.height / 2,
                                    width=3,
                                    fill='blue',
                                    capstyle=ROUND,
                                    tag='second')

            center_r = 10
            self.canvas.create_oval(self.width / 2 - center_r,
                                    self.height / 2 - center_r,
                                    self.width / 2 + center_r,
                                    self.height / 2 + center_r,
                                    fill='white',
                                    tag='center')
        self.type = type
        self.update()

    def update(self):
        now = time.localtime()
        time_str = time.strftime('%Y.%m.%d %a %p', now)
        self.canvas.itemconfigure('date', text=time_str)
        if self.type=='Digital':
            time_str = time.strftime('%I:%M:%S', now)
            self.canvas.itemconfigure('time', text=time_str)
        else:
            self.draw_hour(now.tm_hour)
            self.draw_minute(now.tm_min)
            self.draw_second(now.tm_sec)

    def draw_second(self, second):
        self.__draw_hand('second', self.width * 0.4, second, 60)

    def draw_minute(self, minute):
        self.__draw_hand('minute', self.width * 0.3, minute, 60)

    def draw_hour(self, hour):
        self.__draw_hand('hour', self.width * 0.25, hour % 12, 12)

    def __draw_hand(self, hand, radius, value, system):
        radians = value / system * 2 * math.pi - math.pi / 2
        self.canvas.coords(hand,
                           self.width / 2, self.height / 2,
                           self.width / 2 + radius * math.cos(radians),
                           self.height / 2 + radius * math.sin(radians))

# create the main window
root = Tk()
root.resizable(False, False)
root.title('Tkinter Clock V1.0')

clock_type = StringVar()
clock_type.set('Digital')

enable_menu = OptionMenu(root, clock_type, 'Digital', 'Analog ')
enable_menu.grid(row = 0, column = 0, sticky=W)

# create canvas
canvas = Canvas(root, height= 400, width= 400, relief=SUNKEN)
canvas.grid(row=1, column=0)
clock = Clock(canvas, 400, 400)

def var_changed(*args):
    clock.set_type(clock_type.get())
# set variable observer.
clock_type.trace_variable('w', var_changed)

timer = Timer(root, 1000, clock.update)
timer.start()

root.mainloop()
timer.stop()