from tkinter import *
from tkinter.font import *
from enum import Enum

#color enum value
class GoColor(Enum):
    WHITE = 0
    BLACK = 1

class GoBoard(Canvas):
    def __init__(self, master, size, span):
        Canvas.__init__(self, master, height=size * span, width=size * span)
        self.size = size
        self.span = span
        # create font
        self.font1 = Font(family='Times', size=12)
        self.__draw_board()
        self.__draw_cursor()
        self.step = 0

    def clear(self):
        self.step = 0

    def add_go(self):
        row, col = self.get_cursor()
        r = 11
        if self.step % 2 == 0:
            go_color = 'black'
        else:
            go_color = 'white'
        # add go shape
        self.create_oval(self.__oval_rect(row, col),
                         fill=go_color,
                         tags=['go',
                               'go_oval',
                               self.__oval_tag(row, col),
                               'step' + str(self.step)])
        # move cursor to upmost
        self.tag_raise('cursor', 'go')
        self.step += 1

    def del_go(self):
        row, col = self.get_cursor()
        tag = self.__oval_tag(row, col)
        if self.find_withtag(tag):
            self.delete(tag)
        tag = self.__font_tag(row, col)
        if self.find_withtag(tag):
            self.delete(tag)

    def reset_numbers(self):
        row, col = self.get_cursor()
        self.delete('go_number')
        tags = self.gettags(self.__oval_tag(row, col))
        number = 1
        if tags:
            start_step = int(tags[3][4:])
            for s in range(start_step, self.step):
                tag = 'step{}'.format(s)
                if self.find_withtag(tag):
                    row, col = self.to_rc(self.coords(tag))
                    self.set_number(row, col, number)
                    number += 1

    def set_number(self, row, col, number):
        if number > 0:
            tag = self.__oval_tag(row, col)
            if self.find_withtag(tag):
                if self.itemcget(tag, 'fill') == 'white':
                    font_color = 'black'
                else:
                    font_color = 'white'
                self.create_text(self.span / 2 + col * self.span,
                                 self.span / 2 + row * self.span,
                                 font=self.font1, fill=font_color,
                                 text=str(number),
                                 tags=['go', 'go_number', self.__font_tag(row, col)])
        # move cursor to upmost
        self.tag_raise('cursor', 'go')

    def move_cursor(self, offset_r, offset_c):
        row, col = self.get_cursor()
        row += offset_r
        col += offset_c
        if 0 < col < self.size and 0 < row < self.size:
            self.move('cursor', offset_c * self.span, offset_r * self.span)

    def get_cursor(self):
        coords = self.coords('cursor')
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        return int((y - self.span / 2) / self.span), int((x - self.span / 2) / self.span)

    def to_rc(self, coords):
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        return int((y - self.span / 2) / self.span), int((x - self.span / 2) / self.span)

    def __oval_tag(self, row, col):
        return 'go_oval{},{}'.format(row,col)

    def __font_tag(self, row, col):
        return 'go_number{},{}'.format(row,col)

    def __draw_cursor(self):
        # add go shape
        side = 5
        self.create_rectangle(self.__cursor_rect(int(self.size / 2), int(self.size / 2)),
                              tag='cursor',
                              fill='white')

    def __cursor_rect(self, row, col):
        side = 5
        return self.span / 2 + col * self.span - side,\
               self.span / 2 + row * self.span - side,\
               self.span / 2 + col * self.span + side,\
               self.span / 2 + row * self.span + side

    def __oval_rect(self, row, col):
        side = 11
        return self.span / 2 + col * self.span - side,\
               self.span / 2 + row * self.span - side,\
               self.span / 2 + col * self.span + side,\
               self.span / 2 + row * self.span + side
        
    def __draw_board(self):
        # crate pan
        self.create_rectangle(self.span / 2,
                              self.span / 2,
                              self.span * self.size - self.span / 2,
                              self.span * self.size - self.span / 2,
                              fill='#eeaa40')
        # draw horizental lines
        for r in range(0, self.size):
            self.create_line(self.span / 2,
                               self.span / 2 + r * self.span,
                               self.span * self.size - self.span / 2,
                               self.span / 2 + r * self.span)
        # draw vertical lines
        for c in range(0, self.size):
            self.create_line(self.span / 2 + c * self.span, self.span / 2,
                               self.span / 2 + c * self.span, self.span * self.size - self.span / 2)

# create the main window
root = Tk()
go_board = GoBoard(root, 13, 40)
go_board.grid(row = 0, column = 0)
root.bind_all('<Key-Up>', lambda event:go_board.move_cursor(-1, 0))
root.bind_all('<Key-Down>', lambda event:go_board.move_cursor(1, 0))
root.bind_all('<Key-Left>', lambda event:go_board.move_cursor(0, -1))
root.bind_all('<Key-Right>', lambda event:go_board.move_cursor(0, 1))
root.bind_all('<Key-Insert>', lambda event:go_board.add_go())
root.bind_all('<Key-Delete>', lambda event:go_board.del_go())
root.bind_all('<Key-Home>', lambda event:go_board.reset_numbers())

root.mainloop()